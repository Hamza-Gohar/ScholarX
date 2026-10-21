import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  staticPageGenerationTimeout: 180,
  eslint: {
    ignoreDuringBuilds: true,
  },
  outputFileTracingIncludes: {
    "/api/**/*": ["./data/**/*"],
  },
  async rewrites() {
    return [
      {
        source: "/slides",
        destination: "/slides/index.html",
      },
    ];
  },
};

export default nextConfig;
