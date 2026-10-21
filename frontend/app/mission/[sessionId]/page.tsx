import type { Metadata } from "next";
import { CommandTheatreClient } from "@/components/theatre/CommandTheatreClient";

export const metadata: Metadata = {
  title: "Mission Session",
  robots: {
    index: false,
    follow: false,
  },
};

export default async function MissionPage(props: {
  params: Promise<{ sessionId: string }>;
}) {
  const { sessionId } = await props.params;

  return (
    <CommandTheatreClient
      initialMode="LIVE"
      initialSessionId={sessionId}
    />
  );
}
