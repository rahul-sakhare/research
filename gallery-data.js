// ==========================================================================
// VISUAL CHRONICLE DATA STORE — Rahul Sakhare, Ph.D., P.E.
// ==========================================================================
// This file stores the photographic and documentary record of conference
// podium sessions, invited lectures, poster presentations, technical workshops,
// milestones, and field deployments.
//
// HOW TO ADD PHOTOS:
// 1. Copy your photo to: research/assets/img/gallery/ (e.g. 2026_trb_podium.jpg)
// 2. Add an entry object below inside the window.GALLERY array.
// 3. Run push_updates.bat to publish to the research website.
//
// ENTRY SCHEMA REFERENCE:
// {
//   id: "trb-2026-podium",            // Unique slug string for anchor linking
//   year: 2026,                       // Numeric year (2026, 2025, 2024, 2023, 2022)
//   date: "January 2026",             // Display date string (e.g., "January 2026")
//   category: "podium",               // Category: "podium" | "poster" | "workshop" | "awards" | "field"
//   badge: "Podium Session",          // Badge label shown on the photo
//   event: "TRB 105th Annual Meeting",// Event, conference, or workshop name
//   location: "Washington, D.C.",      // City, State or Venue
//   caption: "Presenting on...",      // Description of the talk, session, or milestone
//   people: ["Dr. Darcy Bullock", ...],// List of co-authors / attendees (optional, pass [] if none)
//   image: "assets/img/gallery/...",  // Relative path to image file (leave null if no photo)
//   link: "https://...",              // Program or publication link (optional, leave null if none)
//   highlight: true                   // true = Top 4-5 curated highlights; false = revealed via "+ Discover More"
// }
// ==========================================================================

window.GALLERY = [
  /*
  // TEMPLATE EXAMPLE (Uncomment and duplicate as you add actual photos):
  {
    id: "trb-2026-podium",
    year: 2026,
    date: "January 2026",
    category: "podium",
    badge: "Podium Session",
    event: "TRB 105th Annual Meeting",
    location: "Washington, D.C.",
    caption: "Presenting on connected vehicle work zone safety analytics.",
    people: ["Dr. Darcy Bullock", "Dr. Jairaj Desai"],
    image: "assets/img/gallery/2026_trb_podium.jpg",
    link: "https://annualmeeting.mytrb.org/",
    highlight: true
  }
  */
];
