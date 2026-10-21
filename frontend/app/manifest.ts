import { MetadataRoute } from "next";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: "ScholarX — Autonomous Scholarship Intelligence Network",
    short_name: "ScholarX",
    description: "Autonomous multi-agent scholarship intelligence system for Pakistani and international students.",
    start_url: "/",
    display: "standalone",
    background_color: "#08080A",
    theme_color: "#18181B",
    icons: [
      {
        src: "/favicon.ico",
        sizes: "any",
        type: "image/x-icon",
      },
    ],
  };
}
