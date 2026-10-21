"use client";

import React, { useEffect, useRef } from "react";
import * as THREE from "three";
import { useCommandStore } from "@/lib/store";

interface ArcItem {
  line: THREE.Line<THREE.BufferGeometry, THREE.LineBasicMaterial>;
  pin: THREE.Mesh<THREE.SphereGeometry, THREE.MeshBasicMaterial>;
}

export const Orbital3DGlobe: React.FC = () => {
  const containerRef = useRef<HTMLDivElement>(null);
  const arcItemsRef = useRef<{ [key: string]: ArcItem }>({});
  const { scouts } = useCommandStore();

  useEffect(() => {
    if (!containerRef.current) return;
    const container = containerRef.current;
    const width = container.clientWidth || 800;
    const height = container.clientHeight || 500;

    // Scene, Camera, Renderer
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    camera.position.z = 240;

    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: "high-performance" });
    renderer.setSize(width, height);
    // Cap pixel ratio at 1.5 for silky smooth, thermal-throttling-free mobile 60fps rendering
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
    container.innerHTML = "";
    container.appendChild(renderer.domElement);

    // Group for globe and arcs
    const globeGroup = new THREE.Group();
    scene.add(globeGroup);

    // Initial orientation to face Pakistan (approx lon 70, lat 30)
    globeGroup.rotation.y = -Math.PI * 0.45;
    globeGroup.rotation.x = 0.25;

    // Base Sphere (Obsidian dark core)
    const radius = 75;
    const sphereGeo = new THREE.SphereGeometry(radius, 48, 48);
    const sphereMat = new THREE.MeshBasicMaterial({
      color: 0x050b14,
      wireframe: false,
    });
    const sphereMesh = new THREE.Mesh(sphereGeo, sphereMat);
    globeGroup.add(sphereMesh);

    // Wireframe Grid (Tactical Lat/Lon lines)
    const wireMat = new THREE.MeshBasicMaterial({
      color: 0x00f0ff,
      wireframe: true,
      transparent: true,
      opacity: 0.12,
    });
    const wireMesh = new THREE.Mesh(sphereGeo, wireMat);
    globeGroup.add(wireMesh);

    // Outer Atmospheric Glow
    const haloGeo = new THREE.SphereGeometry(radius * 1.08, 32, 32);
    const haloMat = new THREE.MeshBasicMaterial({
      color: 0x00f0ff,
      transparent: true,
      opacity: 0.05,
      side: THREE.BackSide,
    });
    const haloMesh = new THREE.Mesh(haloGeo, haloMat);
    globeGroup.add(haloMesh);

    // Convert Geo-coordinates (lat, lon) to 3D Cartesian coordinates
    const latLonToVector3 = (lat: number, lon: number, r: number) => {
      const phi = (90 - lat) * (Math.PI / 180);
      const theta = (lon + 180) * (Math.PI / 180);
      const x = -(r * Math.sin(phi) * Math.cos(theta));
      const z = r * Math.sin(phi) * Math.sin(theta);
      const y = r * Math.cos(phi);
      return new THREE.Vector3(x, y, z);
    };

    // Pakistan Beacon Pin (Green Glowing Sphere)
    const pakPos = latLonToVector3(30.3753, 69.3451, radius);
    const pakGeo = new THREE.SphereGeometry(2.5, 16, 16);
    const pakMat = new THREE.MeshBasicMaterial({ color: 0x00ff88 });
    const pakMesh = new THREE.Mesh(pakGeo, pakMat);
    pakMesh.position.copy(pakPos);
    globeGroup.add(pakMesh);

    // Regional target coordinates
    const targets = [
      { name: "Europe", lat: 52.52, lon: 13.405 },
      { name: "Asia", lat: 39.9042, lon: 116.4074 },
      { name: "Americas", lat: 38.9072, lon: -77.0369 },
      { name: "MENA", lat: 24.7136, lon: 46.6753 },
      { name: "Oceania", lat: -35.2809, lon: 149.13 },
    ];

    // Build 3D Quadratic Bezier Arcs from Pakistan to each target
    const createdItems: { [key: string]: ArcItem } = {};

    targets.forEach((target) => {
      const targetPos = latLonToVector3(target.lat, target.lon, radius);

      // Midpoint projected outward
      const mid = new THREE.Vector3().addVectors(pakPos, targetPos).multiplyScalar(0.5);
      const dist = pakPos.distanceTo(targetPos);
      mid.normalize().multiplyScalar(radius + dist * 0.35);

      const curve = new THREE.QuadraticBezierCurve3(pakPos, mid, targetPos);
      const points = curve.getPoints(50);
      const curveGeo = new THREE.BufferGeometry().setFromPoints(points);
      const curveMat = new THREE.LineBasicMaterial({
        color: 0x1f2937,
        transparent: true,
        opacity: 0.25,
        linewidth: 1.5,
      });
      const arcLine = new THREE.Line(curveGeo, curveMat);
      globeGroup.add(arcLine);

      // Target pin
      const tGeo = new THREE.SphereGeometry(1.5, 12, 12);
      const tMat = new THREE.MeshBasicMaterial({
        color: 0x475569,
      });
      const tMesh = new THREE.Mesh(tGeo, tMat);
      tMesh.position.copy(targetPos);
      globeGroup.add(tMesh);

      createdItems[target.name] = { line: arcLine, pin: tMesh };
    });

    arcItemsRef.current = createdItems;

    // Mouse & Touch Drag Interaction
    let isDragging = false;
    let prevMousePos = { x: 0, y: 0 };

    const onMouseDown = (e: MouseEvent) => {
      isDragging = true;
      prevMousePos = { x: e.clientX, y: e.clientY };
    };

    const onMouseMove = (e: MouseEvent) => {
      if (!isDragging) return;
      const deltaX = e.clientX - prevMousePos.x;
      const deltaY = e.clientY - prevMousePos.y;

      globeGroup.rotation.y += deltaX * 0.006;
      globeGroup.rotation.x += deltaY * 0.006;

      prevMousePos = { x: e.clientX, y: e.clientY };
    };

    const onMouseUp = () => {
      isDragging = false;
    };

    const onTouchStart = (e: TouchEvent) => {
      if (e.touches.length === 1) {
        isDragging = true;
        prevMousePos = { x: e.touches[0].clientX, y: e.touches[0].clientY };
      }
    };

    const onTouchMove = (e: TouchEvent) => {
      if (!isDragging || e.touches.length !== 1) return;
      const deltaX = e.touches[0].clientX - prevMousePos.x;
      const deltaY = e.touches[0].clientY - prevMousePos.y;

      globeGroup.rotation.y += deltaX * 0.006;
      globeGroup.rotation.x += deltaY * 0.006;

      prevMousePos = { x: e.touches[0].clientX, y: e.touches[0].clientY };
    };

    const onTouchEnd = () => {
      isDragging = false;
    };

    container.addEventListener("mousedown", onMouseDown);
    window.addEventListener("mousemove", onMouseMove);
    window.addEventListener("mouseup", onMouseUp);

    container.addEventListener("touchstart", onTouchStart, { passive: true });
    window.addEventListener("touchmove", onTouchMove, { passive: true });
    window.addEventListener("touchend", onTouchEnd);
    window.addEventListener("touchcancel", onTouchEnd);

    // Animation Loop
    let animId: number;
    const animate = () => {
      animId = requestAnimationFrame(animate);
      if (!isDragging) {
        globeGroup.rotation.y += 0.0015; // gentle ambient orbit
      }
      renderer.render(scene, camera);
    };
    animate();

    const handleResize = () => {
      if (!container) return;
      const newW = container.clientWidth;
      const newH = container.clientHeight;
      camera.aspect = newW / newH;
      camera.updateProjectionMatrix();
      renderer.setSize(newW, newH);
    };
    window.addEventListener("resize", handleResize);

    return () => {
      cancelAnimationFrame(animId);
      container.removeEventListener("mousedown", onMouseDown);
      window.removeEventListener("mousemove", onMouseMove);
      window.removeEventListener("mouseup", onMouseUp);
      container.removeEventListener("touchstart", onTouchStart);
      window.removeEventListener("touchmove", onTouchMove);
      window.removeEventListener("touchend", onTouchEnd);
      window.removeEventListener("touchcancel", onTouchEnd);
      window.removeEventListener("resize", handleResize);
      renderer.dispose();
      arcItemsRef.current = {};
    };
  }, []);

  // 2. Reactive Telemetry Updates without re-initializing WebGL Context
  useEffect(() => {
    const items = arcItemsRef.current;
    if (!items || Object.keys(items).length === 0) return;

    const regions: Array<keyof typeof scouts> = ["Europe", "Asia", "Americas", "MENA", "Oceania"];
    regions.forEach((regionName) => {
      const item = items[regionName];
      if (!item) return;

      const scoutState = scouts[regionName];
      const active = scoutState && scoutState.status !== "IDLE";

      item.line.material.color.setHex(active ? 0x00f0ff : 0x1f2937);
      item.line.material.opacity = active ? 0.85 : 0.25;
      item.pin.material.color.setHex(active ? 0x00f0ff : 0x475569);
      item.pin.scale.setScalar(active ? 1.5 : 1.0);
    });
  }, [scouts]);

  return (
    <div className="relative w-full h-full flex items-center justify-center bg-obsidian-950/90 cursor-grab active:cursor-grabbing touch-none select-none">
      <div ref={containerRef} className="w-full h-full" />
      <div className="absolute bottom-3 left-3 sm:bottom-4 sm:left-4 font-mono text-[9px] sm:text-[10px] text-cyber-cyan/50 pointer-events-none tracking-wider bg-black/40 px-2 py-1 rounded backdrop-blur-sm border border-cyber-cyan/10">
        DRAG / TOUCH TO ORBIT // THREE.JS 3D PROJECTION
      </div>
    </div>
  );
};
