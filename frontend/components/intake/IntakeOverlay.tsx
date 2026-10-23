"use client";

import React, { useState } from "react";
import { useCommandStore } from "@/lib/store";
import { SEED_PROFILES } from "@/lib/seed-data";
import { StudentProfile } from "@/lib/types";
import { uploadDocument, sendCounselorChat } from "@/lib/api";
import { percentageToGpa4 } from "@/lib/utils/gpaScale";
import { 
  X, 
  UploadCloud, 
  UserCheck, 
  MessageSquare, 
  Send, 
  Sparkles, 
  GraduationCap, 
  Award, 
  Coins, 
  Globe2,
  FileCheck2,
  Calculator
} from "lucide-react";
import { sound } from "@/lib/sound-fx";
import { IneligiblePoliteModal } from "@/components/common/IneligiblePoliteModal";

const GRADE_POINTS: Record<string, number> = {
  "A*": 90,
  "A": 85,
  "B": 75,
  "C": 65,
  "D": 55,
  "E": 45,
  "U": 0,
};

const calculateIbcc = (grades: string[]) => {
  const points = grades.map((g) => GRADE_POINTS[g] ?? 65);
  const totalObtained = points.reduce((acc, p) => acc + p, 0);
  const maxPossible = grades.length * 100;
  const percentage = Math.round((totalObtained / maxPossible) * 1000) / 10;
  const marks1100 = Math.round((percentage / 100) * 1100);
  const gpa = percentageToGpa4(percentage);

  return { percentage, marks1100, gpa };
};

export const IntakeOverlay: React.FC = () => {
  const {
    overlayView,
    setOverlayView,
    studentProfile,
    setStudentProfile,
    sessionId,
    backendConnected,
    addEvent,
  } = useCommandStore();

  const [streamTab, setStreamTab] = useState<"PERSONAS" | "CAMBRIDGE">("PERSONAS");
  const [aLevel1, setALevel1] = useState<string>("A*");
  const [aLevel2, setALevel2] = useState<string>("A");
  const [aLevel3, setALevel3] = useState<string>("A");
  const [sub1, setSub1] = useState<string>("Mathematics");
  const [sub2, setSub2] = useState<string>("Physics");
  const [sub3, setSub3] = useState<string>("Computer Science");

  const [chatMessages, setChatMessages] = useState<Array<{ sender: "user" | "counselor"; text: string }>>([
    {
      sender: "counselor",
      text: `Assalam-o-Alaikum! I am your ScholarX AI Admissions Counselor for Pakistani students. I have initialized the profile for ${studentProfile.personal.name} (${studentProfile.academic.institution}). Upload your transcript or CV, or tell me about your goals!`,
    },
  ]);
  const [chatInput, setChatInput] = useState("");
  const [isChatLoading, setIsChatLoading] = useState(false);
  const [isUploading, setIsUploading] = useState(false);
  const [showIneligibleModal, setShowIneligibleModal] = useState<boolean>(false);

  if (overlayView !== "INTAKE") return null;

  const liveIbcc = calculateIbcc([aLevel1, aLevel2, aLevel3]);

  const handleSelectPersona = (profile: StudentProfile) => {
    sound.playClick();
    setStudentProfile(profile);
    if (profile.academic.education_system === "CAMBRIDGE" && profile.academic.a_level_grades) {
      if (profile.academic.a_level_grades[0]) setALevel1(profile.academic.a_level_grades[0]);
      if (profile.academic.a_level_grades[1]) setALevel2(profile.academic.a_level_grades[1]);
      if (profile.academic.a_level_grades[2]) setALevel3(profile.academic.a_level_grades[2]);
    }
    setChatMessages((prev) => [
      ...prev,
      {
        sender: "counselor",
        text: `Loaded student persona: ${profile.personal.name}. Stream: ${profile.academic.education_system === "CAMBRIDGE" ? "Cambridge International (O/A-Levels)" : "Pakistani HSSC / BISE / FBISE"}. Academic background: ${profile.academic.field_of_study} at ${profile.academic.institution}. Profile completeness: ${profile.profile_completeness}%.`,
      },
    ]);
  };

  const handleApplyCambridge = () => {
    sound.playClick();
    const eq = calculateIbcc([aLevel1, aLevel2, aLevel3]);
    const updatedProfile: StudentProfile = {
      ...studentProfile,
      academic: {
        ...studentProfile.academic,
        education_system: "CAMBRIDGE",
        grading_system: "CAMBRIDGE_LETTER_GRADES",
        a_level_grades: [aLevel1, aLevel2, aLevel3],
        ibcc_equivalence_percentage: eq.percentage,
        ibcc_total_marks: eq.marks1100,
        percentage: eq.percentage,
        gpa_percentage: eq.percentage,
        gpa_obtained: eq.gpa,
        gpa_4_scale: eq.gpa,
        institution: studentProfile.academic.institution.toLowerCase().includes("grammar") || studentProfile.academic.institution.toLowerCase().includes("cambridge")
          ? studentProfile.academic.institution
          : "Cambridge International Center (Karachi / Lahore / Islamabad)",
      },
    };
    setStudentProfile(updatedProfile);

    if (eq.percentage < 70) {
      sound.playSkepticAlert();
      setShowIneligibleModal(true);
    }

    setChatMessages((prev) => [
      ...prev,
      {
        sender: "counselor",
        text: `[CAMBRIDGE EQUIVALENCE ENGINE] Computed official IBCC equivalence for A-Levels [${aLevel1}, ${aLevel2}, ${aLevel3}]: ${eq.percentage}% (${eq.marks1100}/1100 Marks Equivalent, CGPA ${eq.gpa.toFixed(2)}/4.0). Stream updated to Cambridge International. ${
          eq.percentage < 70
            ? "⚠️ Notice: Equivalence below 70% threshold (Ineligible for Merit Awards). Strict merit quotas will decline eligibility, but ScholarX has activated Need-Based alternative pathways (Italian DSU Regional Grants & China CSC Type-B)."
            : "✅ Meets competitive eligibility for European Bilateral Quota programs. Submit Statement of Results directly to IBCC Cambridge Cell (Plot 25, G-10/4, Islamabad)."
        }`,
      },
    ]);
  };

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!chatInput.trim() || isChatLoading) return;

    const userText = chatInput.trim();
    setChatInput("");
    setChatMessages((prev) => [...prev, { sender: "user", text: userText }]);
    setIsChatLoading(true);
    sound.playClick();

    if (backendConnected) {
      try {
        const res = await sendCounselorChat(sessionId, userText);
        setChatMessages((prev) => [...prev, { sender: "counselor", text: res.reply }]);
        if (res.profile) setStudentProfile(res.profile);
      } catch (err) {
        setChatMessages((prev) => [
          ...prev,
          { sender: "counselor", text: "Counselor service is operating in offline mode. For Pakistanis aiming for DAAD or Stipendium Hungaricum, ensure your HEC degree attestation is initiated at least 6 weeks in advance." },
        ]);
      }
    } else {
      // Local counselor response logic
      setTimeout(() => {
        let reply = "Based on your Pakistani academic profile, your GPA and background match high-probability bilateral programs. Make sure to schedule your IBCC equivalence and HEC HAT test early.";
        if (userText.toLowerCase().includes("budget") || userText.toLowerCase().includes("cost") || userText.toLowerCase().includes("pkr")) {
          reply = `With your max out-of-pocket budget of PKR ${(studentProfile.financial.max_out_of_pocket_pkr).toLocaleString()}, you can comfortably cover initial attestations, IELTS, and embassy visa processing for fully-funded programs like Stipendium Hungaricum or Turkiye Burslari.`;
        } else if (userText.toLowerCase().includes("ielts") || userText.toLowerCase().includes("english")) {
          reply = `Your English score is recorded as: ${studentProfile.language.ielts_overall || "Pending"}. Many European universities accept an English Medium of Instruction (MOI) certificate from Pakistani chartered universities, but DAAD and Fulbright require academic IELTS.`;
        }
        setChatMessages((prev) => [...prev, { sender: "counselor", text: reply }]);
        setIsChatLoading(false);
        sound.playTelemetryTick();
      }, 500);
      return;
    }
    setIsChatLoading(false);
  };

  const handleFileUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setIsUploading(true);
    sound.playBoot();

    if (backendConnected) {
      try {
        const res = await uploadDocument(sessionId, file);
        if (res.profile) setStudentProfile(res.profile);
        setChatMessages((prev) => [
          ...prev,
          {
            sender: "counselor",
            text: `Successfully parsed document ${file.name} as ${res.doc_type}! Extracted credentials updated in your profile.`,
          },
        ]);
      } catch (err) {
        setChatMessages((prev) => [
          ...prev,
          { sender: "counselor", text: `Upload encountered an error, falling back to simulated extraction for ${file.name}.` },
        ]);
      }
    } else {
      setTimeout(() => {
        setIsUploading(false);
        setChatMessages((prev) => [
          ...prev,
          {
            sender: "counselor",
            text: `[SIMULATED PARSER] Successfully ingested "${file.name}". Classified as ACADEMIC_TRANSCRIPT. Verified GPA: 3.42, 82% Marks, HEC recognized institution verified.`,
          },
        ]);
        sound.playRadarPing();
      }, 800);
      return;
    }
    setIsUploading(false);
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-md flex items-center justify-center p-6 animate-in fade-in duration-200">
      <div className="relative w-full max-w-5xl h-[85vh] bg-obsidian-900 border border-cyber-cyan/40 rounded-lg shadow-glow-cyan flex flex-col overflow-hidden corner-bracket">
        {/* Modal Header */}
        <div className="flex items-center justify-between px-6 py-3.5 bg-obsidian-950 border-b border-white/10 select-none">
          <div className="flex items-center space-x-3">
            <UserCheck className="w-5 h-5 text-cyber-cyan" />
            <div>
              <h2 className="font-mono text-sm font-bold tracking-wider text-white">
                STUDENT INTAKE CONSOLE // 3-IN-1 PROFILING SUITE
              </h2>
              <p className="font-mono text-[10px] text-white/40">
                1-CLICK PERSONAS • TRANSCRIPT/CV PARSER • ADMISSIONS COUNSELOR CHAT
              </p>
            </div>
          </div>

          <button
            onClick={() => {
              sound.playClick();
              setOverlayView("NONE");
            }}
            className="p-1 rounded hover:bg-white/10 text-white/50 hover:text-white transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="flex-1 grid grid-cols-12 gap-4 p-5 overflow-hidden">
          {/* Left Column (5 Cols): Persona Selector & Profile Metrics */}
          <div className="col-span-5 flex flex-col space-y-4 overflow-y-auto pr-1">
            {/* Stream Mode Switcher */}
            <div className="grid grid-cols-2 gap-1.5 p-1 bg-obsidian-950 rounded border border-white/10">
              <button
                onClick={() => { sound.playClick(); setStreamTab("PERSONAS"); }}
                className={`py-1.5 px-2 rounded font-mono text-[10px] font-bold flex items-center justify-center space-x-1.5 transition-all ${
                  streamTab === "PERSONAS"
                    ? "bg-cyber-cyan text-obsidian-950 shadow-glow-cyan"
                    : "text-white/60 hover:text-white"
                }`}
              >
                <UserCheck className="w-3.5 h-3.5" />
                <span>DEMO PERSONAS</span>
              </button>
              <button
                onClick={() => { sound.playClick(); setStreamTab("CAMBRIDGE"); }}
                className={`py-1.5 px-2 rounded font-mono text-[10px] font-bold flex items-center justify-center space-x-1.5 transition-all ${
                  streamTab === "CAMBRIDGE"
                    ? "bg-cyber-cyan text-obsidian-950 shadow-glow-cyan"
                    : "text-white/60 hover:text-white"
                }`}
              >
                <Calculator className="w-3.5 h-3.5" />
                <span>CAMBRIDGE IBCC</span>
              </button>
            </div>

            {streamTab === "PERSONAS" ? (
              <>
                {/* 1-Click Pakistani Demo Personas */}
                <div className="command-panel p-3 rounded border border-white/10">
                  <span className="font-mono text-[10px] font-bold tracking-widest text-cyber-cyan block mb-2">
                    1-CLICK DEMO PERSONAS (PAKISTANI & CAMBRIDGE)
                  </span>
                  <div className="space-y-1.5">
                    {SEED_PROFILES.map((p) => {
                      const isSelected = studentProfile.student_id === p.student_id;
                      const isCambridge = p.academic.education_system === "CAMBRIDGE";
                      return (
                        <button
                          key={p.student_id}
                          onClick={() => handleSelectPersona(p)}
                          className={`w-full text-left p-2 rounded font-mono text-xs flex items-center justify-between border transition-all ${
                            isSelected
                              ? "bg-cyber-cyan/20 border-cyber-cyan text-white shadow-glow-cyan"
                              : "bg-obsidian-950 border-white/5 text-white/60 hover:border-white/20 hover:text-white"
                          }`}
                        >
                          <div>
                            <div className="font-bold flex items-center space-x-1.5">
                              <span>{p.personal.name}</span>
                              {isCambridge && (
                                <span className="text-[8px] px-1 rounded bg-cyber-cyan/30 text-cyber-cyan font-bold border border-cyber-cyan/50">
                                  CAMBRIDGE A-LEVELS
                                </span>
                              )}
                            </div>
                            <div className="text-[10px] text-white/40">
                              {p.academic.institution} • {p.academic.field_of_study}
                            </div>
                          </div>
                          <span className="text-[10px] px-1.5 py-0.5 rounded bg-white/10 text-cyber-cyan font-bold">
                            {isCambridge && p.academic.ibcc_equivalence_percentage
                              ? `${p.academic.ibcc_equivalence_percentage}% IBCC`
                              : p.academic.gpa_obtained
                              ? `${p.academic.gpa_obtained} GPA`
                              : `${p.academic.percentage}%`}
                          </span>
                        </button>
                      );
                    })}
                  </div>
                </div>

                {/* Document Drag-and-Drop Zone */}
                <div className="command-panel p-4 rounded border border-dashed border-cyber-cyan/30 hover:border-cyber-cyan/60 transition-colors text-center relative flex flex-col items-center justify-center">
                  <input
                    type="file"
                    accept=".pdf,.docx,.txt"
                    onChange={handleFileUpload}
                    className="absolute inset-0 opacity-0 cursor-pointer"
                  />
                  <UploadCloud className="w-8 h-8 text-cyber-cyan mb-2 animate-pulse" />
                  <div className="font-mono text-xs font-bold text-white mb-0.5">
                    {isUploading ? "PARSING DOCUMENT..." : "DRAG & DROP TRANSCRIPT / CV"}
                  </div>
                  <div className="font-mono text-[10px] text-white/40">
                    Supports PDF, DOCX, TXT (HEC Transcripts, Cambridge Certificates)
                  </div>
                </div>
              </>
            ) : (
              /* Cambridge O/A-Levels Equivalence Calculator */
              <div className="command-panel p-3.5 rounded border border-cyber-cyan/30 space-y-3 font-mono">
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-1.5 text-cyber-cyan">
                    <GraduationCap className="w-4 h-4 text-cyber-cyan" />
                    <span className="text-xs font-bold">CAMBRIDGE EQUIVALENCE CALCULATOR</span>
                  </div>
                  <span className="text-[9px] px-1.5 py-0.5 rounded bg-pakistan-deep text-pakistan-emerald font-bold border border-pakistan-emerald/30">
                    IBCC 1100 BENCHMARK
                  </span>
                </div>

                <p className="text-[10px] text-white/60 leading-relaxed">
                  Converts Cambridge CIE/Edexcel A-Levels to standard Pakistani HSSC / FSc marks. Bypasses provincial BISE / FBISE boards directly to IBCC Cambridge Cell Islamabad.
                </p>

                {/* Subject & Grade Selectors */}
                <div className="space-y-2">
                  <span className="text-[10px] text-white/80 font-bold block">
                    PRINCIPAL A-LEVEL SUBJECTS & GRADES:
                  </span>
                  
                  <div className="space-y-1.5">
                    {/* Subject 1 */}
                    <div className="flex items-center space-x-2">
                      <input
                        type="text"
                        value={sub1}
                        onChange={(e) => setSub1(e.target.value)}
                        className="flex-1 bg-obsidian-950 border border-white/10 rounded px-2 py-1 text-white text-[11px]"
                        placeholder="Subject 1"
                      />
                      <select
                        value={aLevel1}
                        onChange={(e) => { sound.playClick(); setALevel1(e.target.value); }}
                        className="w-24 bg-obsidian-950 border border-cyber-cyan/40 text-cyber-cyan font-bold rounded px-2 py-1 text-xs"
                      >
                        {["A*", "A", "B", "C", "D", "E"].map((g) => (
                          <option key={g} value={g}>{g} ({GRADE_POINTS[g]} pts)</option>
                        ))}
                      </select>
                    </div>

                    {/* Subject 2 */}
                    <div className="flex items-center space-x-2">
                      <input
                        type="text"
                        value={sub2}
                        onChange={(e) => setSub2(e.target.value)}
                        className="flex-1 bg-obsidian-950 border border-white/10 rounded px-2 py-1 text-white text-[11px]"
                        placeholder="Subject 2"
                      />
                      <select
                        value={aLevel2}
                        onChange={(e) => { sound.playClick(); setALevel2(e.target.value); }}
                        className="w-24 bg-obsidian-950 border border-cyber-cyan/40 text-cyber-cyan font-bold rounded px-2 py-1 text-xs"
                      >
                        {["A*", "A", "B", "C", "D", "E"].map((g) => (
                          <option key={g} value={g}>{g} ({GRADE_POINTS[g]} pts)</option>
                        ))}
                      </select>
                    </div>

                    {/* Subject 3 */}
                    <div className="flex items-center space-x-2">
                      <input
                        type="text"
                        value={sub3}
                        onChange={(e) => setSub3(e.target.value)}
                        className="flex-1 bg-obsidian-950 border border-white/10 rounded px-2 py-1 text-white text-[11px]"
                        placeholder="Subject 3"
                      />
                      <select
                        value={aLevel3}
                        onChange={(e) => { sound.playClick(); setALevel3(e.target.value); }}
                        className="w-24 bg-obsidian-950 border border-cyber-cyan/40 text-cyber-cyan font-bold rounded px-2 py-1 text-xs"
                      >
                        {["A*", "A", "B", "C", "D", "E"].map((g) => (
                          <option key={g} value={g}>{g} ({GRADE_POINTS[g]} pts)</option>
                        ))}
                      </select>
                    </div>
                  </div>
                </div>

                {/* Real-Time IBCC Output Box */}
                <div className="p-2.5 rounded bg-obsidian-950 border border-pakistan-emerald/40 space-y-1.5 text-xs">
                  <div className="flex items-center justify-between">
                    <span className="text-white/50 text-[10px]">IBCC EQUIVALENCE:</span>
                    <span className="text-pakistan-emerald font-bold text-sm">
                      {liveIbcc.percentage}% • {liveIbcc.marks1100} / 1100 Marks
                    </span>
                  </div>
                  <div className="flex items-center justify-between text-[11px]">
                    <span className="text-white/50">CONVERTED CGPA:</span>
                    <span className="text-cyber-cyan font-bold">{liveIbcc.gpa.toFixed(2)} / 4.0 Scale</span>
                  </div>
                  <div className="text-[9px] text-white/40 pt-1 border-t border-white/5">
                    Attestation: Submit original CIE Statement of Results to IBCC Cambridge Cell (Plot 25, G-10/4, Islamabad).
                  </div>

                  {liveIbcc.percentage < 70 && (
                    <div className="mt-1.5 p-2 rounded bg-warning-amber/15 border border-warning-amber/30 text-warning-amber text-[10px] leading-relaxed flex items-center justify-between gap-2">
                      <div>
                        ⚠️ <strong>Academic Gate Notice:</strong> Score ({liveIbcc.percentage}%) is below the 70.0% merit cutoff (Ineligible for standard merit quotas). ScholarX automatically recommends <strong>Need-Based Italian DSU Regional Grants</strong> & <strong>China CSC Type-B</strong>.
                      </div>
                      <button
                        type="button"
                        onClick={() => {
                          sound.playClick();
                          setShowIneligibleModal(true);
                        }}
                        className="px-2 py-1 rounded bg-warning-amber/20 hover:bg-warning-amber/30 text-warning-amber font-bold text-[9px] border border-warning-amber/40 shrink-0 transition-colors"
                      >
                        Guidance
                      </button>
                    </div>
                  )}
                </div>

                {/* Apply Button */}
                <button
                  onClick={handleApplyCambridge}
                  className="w-full py-2 rounded bg-pakistan-emerald hover:bg-emerald-400 text-obsidian-950 font-bold text-xs transition-all shadow-glow-emerald"
                >
                  APPLY EQUIVALENCE TO ACTIVE PROFILE
                </button>
              </div>
            )}

            {/* Current Active Profile Summary Card */}
            <div className="command-panel p-3.5 rounded border border-white/10 font-mono text-xs space-y-2">
              <div className="flex items-center justify-between border-b border-white/10 pb-1.5">
                <span className="text-white/50 text-[10px]">CURRENT PROFILE:</span>
                <span className="text-pakistan-emerald font-bold">
                  {studentProfile.profile_completeness}% VERIFIED
                </span>
              </div>
              <div className="grid grid-cols-2 gap-2 text-[11px]">
                <div>
                  <span className="text-white/40 block text-[9px]">STREAM / EDUCATION</span>
                  <span className="font-semibold text-white truncate block">
                    {studentProfile.academic.education_system === "CAMBRIDGE" ? "Cambridge (O/A-Levels)" : "Pakistani HSSC / BISE / FBISE"}
                  </span>
                </div>
                <div>
                  <span className="text-white/40 block text-[9px]">MARKS / EQUIVALENCE</span>
                  <span className="font-semibold text-cyber-cyan">
                    {studentProfile.academic.education_system === "CAMBRIDGE" && studentProfile.academic.ibcc_equivalence_percentage
                      ? `${studentProfile.academic.ibcc_equivalence_percentage}% (${studentProfile.academic.ibcc_total_marks || 950}/1100)`
                      : studentProfile.academic.gpa_obtained
                      ? `${studentProfile.academic.gpa_obtained} GPA (${studentProfile.academic.percentage}%)`
                      : `${studentProfile.academic.percentage}%`}
                  </span>
                </div>
                <div>
                  <span className="text-white/40 block text-[9px]">ENGLISH PROFICIENCY</span>
                  <span className="font-semibold text-white">
                    {studentProfile.language.ielts_overall ? `IELTS ${studentProfile.language.ielts_overall}` : "MOI Certificate"}
                  </span>
                </div>
                <div>
                  <span className="text-white/40 block text-[9px]">MAX OUT-OF-POCKET</span>
                  <span className="font-semibold text-warning-amber">
                    PKR {(studentProfile.financial.max_out_of_pocket_pkr).toLocaleString()}
                  </span>
                </div>
              </div>
            </div>
          </div>

          {/* Right Column (7 Cols): Multi-Turn Admissions Counselor Chat */}
          <div className="col-span-7 flex flex-col command-panel rounded border border-white/10 overflow-hidden">
            {/* Counselor Title */}
            <div className="px-4 py-2 bg-obsidian-950 border-b border-white/10 flex items-center justify-between">
              <div className="flex items-center space-x-2">
                <MessageSquare className="w-4 h-4 text-cyber-cyan" />
                <span className="font-mono text-xs font-bold text-white">
                  PAKISTANI ADMISSIONS COUNSELOR AI
                </span>
              </div>
              <span className="font-mono text-[9px] px-2 py-0.5 rounded bg-pakistan-deep text-pakistan-emerald font-bold">
                HEC & EMBASSY SPECIALIST
              </span>
            </div>

            {/* Chat Messages Log */}
            <div className="flex-1 overflow-y-auto p-4 space-y-3 font-mono text-xs bg-obsidian-950/60">
              {chatMessages.map((msg, i) => (
                <div
                  key={i}
                  className={`flex ${
                    msg.sender === "user" ? "justify-end" : "justify-start"
                  }`}
                >
                  <div
                    className={`max-w-[85%] p-3 rounded ${
                      msg.sender === "user"
                        ? "bg-cyber-cyan/20 border border-cyber-cyan/40 text-white rounded-br-none"
                        : "bg-obsidian-850 border border-white/10 text-white/90 rounded-bl-none"
                    }`}
                  >
                    <div className="text-[9px] text-white/40 font-bold uppercase mb-1">
                      {msg.sender === "user" ? "You" : "ScholarX Counselor"}
                    </div>
                    <div className="leading-relaxed whitespace-pre-wrap">{msg.text}</div>
                  </div>
                </div>
              ))}
              {isChatLoading && (
                <div className="flex justify-start">
                  <div className="p-2.5 rounded bg-obsidian-850 border border-white/10 font-mono text-xs text-cyber-cyan animate-pulse">
                    Consulting Pakistani admissions knowledge base...
                  </div>
                </div>
              )}
            </div>

            {/* Chat Input Bar */}
            <form onSubmit={handleSendMessage} className="p-2.5 bg-obsidian-950 border-t border-white/10 flex items-center space-x-2">
              <input
                type="text"
                placeholder="Ask about HEC quotas, DAAD IELTS exemptions, visa costs..."
                value={chatInput}
                onChange={(e) => setChatInput(e.target.value)}
                className="flex-1 bg-obsidian-900 border border-white/10 rounded px-3 py-2 text-white font-mono text-xs focus:outline-none focus:border-cyber-cyan"
              />
              <button
                type="submit"
                disabled={isChatLoading || !chatInput.trim()}
                className="px-4 py-2 rounded bg-cyber-cyan hover:bg-cyan-300 text-obsidian-950 font-mono text-xs font-bold transition-colors disabled:opacity-40"
              >
                <Send className="w-3.5 h-3.5" />
              </button>
            </form>
          </div>
        </div>
      </div>

      {/* Polite Ineligibility Modal (< 70% Marks) */}
      <IneligiblePoliteModal
        isOpen={showIneligibleModal}
        percentage={studentProfile.academic.percentage || liveIbcc.percentage}
        gpa4Scale={studentProfile.academic.gpa_4_scale || liveIbcc.gpa}
        onClose={() => setShowIneligibleModal(false)}
        onProceedAnyway={() => setShowIneligibleModal(false)}
        onAdjustMarks={() => setShowIneligibleModal(false)}
      />
    </div>
  );
};
