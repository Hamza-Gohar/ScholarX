import { ImageResponse } from "next/og";

export const alt = "ScholarX — Autonomous Scholarship Intelligence Network";
export const size = {
  width: 1200,
  height: 630,
};
export const contentType = "image/png";

export default function Image() {
  return new ImageResponse(
    (
      <div
        style={{
          background: "#08080A",
          width: "100%",
          height: "100%",
          display: "flex",
          flexDirection: "column",
          alignItems: "flex-start",
          justifyContent: "space-between",
          padding: 80,
          fontFamily: "system-ui, -apple-system, sans-serif",
          position: "relative",
        }}
      >
        <div
          style={{
            position: "absolute",
            top: -100,
            right: -100,
            width: 500,
            height: 500,
            borderRadius: "50%",
            background: "radial-gradient(circle, rgba(56, 189, 248, 0.15) 0%, rgba(0, 0, 0, 0) 70%)",
          }}
        />

        <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
          <div
            style={{
              width: 56,
              height: 56,
              borderRadius: 14,
              background: "#0F172A",
              border: "2px solid #38BDF8",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              color: "#38BDF8",
              fontSize: 32,
              fontWeight: 900,
            }}
          >
            X
          </div>
          <span style={{ fontSize: 32, fontWeight: 800, color: "#F8FAFC", letterSpacing: "-0.02em" }}>
            SCHOLAR<span style={{ color: "#38BDF8" }}>X</span>
          </span>
        </div>

        <div style={{ display: "flex", flexDirection: "column", gap: 20 }}>
          <div
            style={{
              display: "flex",
              alignItems: "center",
              padding: "8px 20px",
              borderRadius: 30,
              background: "rgba(56, 189, 248, 0.1)",
              border: "1px solid rgba(56, 189, 248, 0.3)",
              color: "#38BDF8",
              fontSize: 18,
              fontWeight: 600,
            }}
          >
            Autonomous Scholarship Intelligence Network
          </div>
          <h1
            style={{
              fontSize: 56,
              fontWeight: 900,
              color: "#FFFFFF",
              lineHeight: 1.15,
              maxWidth: 950,
              margin: 0,
              letterSpacing: "-0.03em",
            }}
          >
            310+ Fully-Funded International Scholarships for Pakistani Students
          </h1>
          <p
            style={{
              fontSize: 24,
              color: "#94A3B8",
              maxWidth: 850,
              margin: 0,
              lineHeight: 1.4,
            }}
          >
            Stipendium Hungaricum • Türkiye Bursları • CSC • DAAD • Fulbright • Chevening • MEXT • KGSP
          </p>
        </div>

        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            width: "100%",
            borderTop: "1px solid #1E293B",
            paddingTop: 30,
            color: "#64748B",
            fontSize: 20,
          }}
        >
          <span>Verified Bilateral Quotas • HEC Attestation • Step-by-Step Roadmaps</span>
          <span style={{ color: "#38BDF8", fontWeight: 700 }}>scholarx.online</span>
        </div>
      </div>
    ),
    {
      ...size,
    }
  );
}
