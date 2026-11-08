// Visual Chronicle Data Store — Rahul Sakhare, Ph.D., P.E.
// Each entry represents a conference presentation, podium session, invited lecture, poster, or field milestone.
// highlight: true denotes the 4-5 curated highlights per year shown by default.
// Additional sessions are revealed when clicking "+ Discover More" for that year or filtering.

window.GALLERY = [
  // ==========================================
  // 2026
  // ==========================================
  {
    id: "trb-2026-podium",
    year: 2026,
    date: "January 2026",
    category: "podium",
    badge: "Podium Session",
    event: "TRB 105th Annual Meeting",
    location: "Washington, D.C.",
    caption: "Presenting on commercial truck dash-cam video analytics for dynamic work zone inspection and worker safety monitoring.",
    people: ["Dr. Darcy Bullock", "Dr. Jairaj Desai", "Myles Overall", "Justin Mukai", "Joshua McGregor"],
    image: "assets/img/gallery/dashcam_yolo.webp",
    link: "https://annualmeeting.mytrb.org/OnlineProgram/Details/24853",
    highlight: true
  },
  {
    id: "road-school-2026-mobility",
    year: 2026,
    date: "March 2026",
    category: "podium",
    badge: "Lectern Session",
    event: "112th Purdue Road School Transportation Conference",
    location: "West Lafayette, IN",
    caption: "Delivering podium lecture on segment mobility and signal performance measures derived from connected vehicle trajectory waypoints.",
    people: ["Rickey Taylor", "INDOT District Traffic Operations"],
    image: "assets/img/gallery/indiana_segment_pm.webp",
    highlight: true
  },
  {
    id: "trb-2026-poster-network",
    year: 2026,
    date: "January 2026",
    category: "poster",
    badge: "Poster Presentation",
    event: "TRB 105th Annual Meeting · Session 24601",
    location: "Washington, D.C.",
    caption: "Engaging with transportation agency engineers on statewide screening for hard-braking and systemwide traffic mobility bottlenecks.",
    people: ["Christopher Gartner", "Nathan Shellhamer", "Dr. Darcy Bullock"],
    image: "assets/img/gallery/heatmap_tool.webp",
    link: "https://annualmeeting.mytrb.org/OnlineProgram/Details/24601",
    highlight: true
  },
  {
    id: "ite-lunch-2026",
    year: 2026,
    date: "February 2026",
    category: "workshop",
    badge: "Invited Talk",
    event: "ITE Indiana Section Technical Series",
    location: "Indianapolis, IN",
    caption: "Invited presentation on connected vehicle data operational use cases for municipal and state transportation practitioners.",
    people: ["Christopher Gartner", "Indiana ITE Leadership"],
    image: "assets/img/gallery/jtrp_research_portrait.jpg",
    link: "https://indianaite.starchapter.com/meetinginfo.php?id=202&ts=1768590344",
    highlight: true
  },
  {
    id: "purdue-ce36100-2026",
    year: 2026,
    date: "April 2026",
    category: "workshop",
    badge: "University Guest Lecture",
    event: "CE 36100 Transportation Engineering · Purdue University",
    location: "West Lafayette, IN",
    caption: "Guest lecture educating emerging civil engineers on high-frequency trajectory applications, work zone safety screening, and statewide performance measures.",
    people: ["Undergraduate Civil Engineering Students"],
    image: "assets/img/gallery/purdue_cv_field_deployment.jpg",
    highlight: true
  },
  {
    id: "road-school-2026-vision",
    year: 2026,
    date: "March 2026",
    category: "podium",
    badge: "Lectern Session",
    event: "112th Purdue Road School · Session 159",
    location: "West Lafayette, IN",
    caption: "Technical presentation evaluating road asset identification technology utilizing commercial truck forward-facing camera imagery.",
    people: ["Andrew Thompson", "Neal Sturdevant"],
    image: "assets/img/gallery/dashcam_llm.webp",
    highlight: false
  },
  {
    id: "trb-2026-speed-control",
    year: 2026,
    date: "January 2026",
    category: "podium",
    badge: "Poster Session",
    event: "TRB 105th Annual Meeting · Session 24522",
    location: "Washington, D.C.",
    caption: "Presenting data-driven evaluation of automated worksite speed enforcement and queue hazard alerting ahead of construction zones.",
    people: ["Dr. Jairaj Desai", "Joshua McGregor", "Brad Snyder", "Dr. Darcy Bullock"],
    image: null,
    link: "https://annualmeeting.mytrb.org/OnlineProgram/Details/24522",
    highlight: false
  },

  // ==========================================
  // 2025
  // ==========================================
  {
    id: "trb-2025-lectern-maintenance",
    year: 2025,
    date: "January 2025",
    category: "podium",
    badge: "Lectern Session",
    event: "TRB 104th Annual Meeting · Session 22915",
    location: "Washington, D.C.",
    caption: "Presenting on innovative use of emerging connected vehicle data and criteria for statewide highway maintenance management.",
    people: ["Dr. Jijo Mathew", "Dr. Jairaj Desai", "John Hunter", "Dr. Darcy Bullock"],
    image: "assets/img/gallery/purdue_cv_field_deployment.jpg",
    link: "https://annualmeeting.mytrb.org/OnlineProgramArchive/Details/22915",
    highlight: true
  },
  {
    id: "usdot-v2x-2025",
    year: 2025,
    date: "December 2025",
    category: "field",
    badge: "USDOT Federal Feature",
    event: "U.S. DOT ITS Joint Program Office",
    location: "Washington, D.C.",
    caption: "Federal showcase on Indiana DOT V2X-equipped queue warning trucks with digital alerts reducing secondary crash hard-braking by 80%.",
    people: ["INDOT Operations", "USDOT ITS JPO", "Purdue JTRP Team"],
    image: "assets/img/gallery/hero_photo.jpg",
    link: "https://www.itskrs.its.dot.gov/success-strategies/snapshot/vehicle-everything-v2x-communications",
    highlight: true
  },
  {
    id: "trb-2025-aashto-award",
    year: 2025,
    date: "January 2025",
    category: "awards",
    badge: "AASHTO High-Value Project",
    event: "TRB 104th Annual Meeting · Session P25-20182",
    location: "Washington, D.C.",
    caption: "Honored at the State DOT Research High-Value Project Winners session for Indiana work zone connected vehicle analytics.",
    people: ["Prof. Darcy Bullock", "State DOT Research Directors"],
    image: "assets/img/gallery/purdue_phd_hooding_2023.png",
    link: "https://annualmeeting.mytrb.org/OnlineProgramArchive/Details/22727",
    highlight: true
  },
  {
    id: "road-school-2025-profiles",
    year: 2025,
    date: "March 2025",
    category: "workshop",
    badge: "Technical Workshop",
    event: "111th Purdue Road School",
    location: "West Lafayette, IN",
    caption: "Presenting multi-year Indiana interstate speed profiles (2020–2024) to district transportation engineers and state police commanders.",
    people: ["Dave Horton", "Dr. Jairaj Desai", "INDOT District Traffic Engineers"],
    image: "assets/img/gallery/indiana_segment_pm.webp",
    highlight: true
  },
  {
    id: "trb-2025-privacy-filters",
    year: 2025,
    date: "January 2025",
    category: "poster",
    badge: "Poster Session",
    event: "TRB 104th Annual Meeting · Session 22967",
    location: "Washington, D.C.",
    caption: "Evaluating impact of privacy filtering and fleet market penetration on connected vehicle trajectory datasets for intersections and freeways.",
    people: ["Enrique Saldivar-Carranza", "Ahsmitha Sivakumar", "Justin Mukai"],
    image: null,
    highlight: false
  },

  // ==========================================
  // 2024
  // ==========================================
  {
    id: "google-innovator-2024",
    year: 2024,
    date: "October 2024",
    category: "awards",
    badge: "Google Cloud Innovator",
    event: "Google Cloud Research Innovators Global Summit",
    location: "Sunnyvale, CA",
    caption: "Selected to the fourth global cohort of Google Cloud Research Innovators for developing cloud-native spatial-temporal pipelines for traffic telematics.",
    people: ["Google Cloud Public Sector Research Team"],
    image: "assets/img/gallery/google_cloud_innovators_2024.jpg",
    link: "https://cloud.google.com/blog/topics/public-sector/google-cloud-research-innovators-launch-fourth-cohort-to-drive-innovation/#:~:text=Rahul%20Suryakant%20Sakhare",
    highlight: true
  },
  {
    id: "iitm-seminar-2024",
    year: 2024,
    date: "August 2024",
    category: "workshop",
    badge: "Invited International Seminar",
    event: "Department of Civil Engineering, IIT Madras",
    location: "Chennai, India",
    caption: "Delivering invited seminar on kinematic shockwave identification and speed estimation using connected vehicle trajectory data.",
    people: ["Dr. V. Lelitha Devi", "Faculty and Graduate Researchers at IIT Madras Transportation Division"],
    image: "assets/img/gallery/jtrp_research_portrait.jpg",
    highlight: true
  },
  {
    id: "eclipse-operations-2024",
    year: 2024,
    date: "April 2024",
    category: "field",
    badge: "Real-Time Operations & Media",
    event: "Total Solar Eclipse Traffic Monitoring · INDOT TMC",
    location: "Indianapolis, IN",
    caption: "Monitoring national traffic mobility, corridor speeds, and congestion surge during the 2024 total solar eclipse, featured on Fox59.",
    people: ["INDOT TMC Operators", "JTRP Operations Research Team"],
    image: "assets/img/gallery/purdue_cv_field_deployment.jpg",
    link: "https://doi.org/10.1016/j.trip.2024.101225",
    highlight: true
  },
  {
    id: "nyt-feature-2024",
    year: 2024,
    date: "December 2024",
    category: "field",
    badge: "National Press Feature",
    event: "The New York Times Front Page Print Edition",
    location: "National / New York, NY",
    caption: "Front-page feature in the December 21, 2024 print edition spotlighting the Purdue connected-vehicle research group's highway safety innovations.",
    people: ["Prof. Darcy Bullock", "Purdue JTRP Research Team"],
    image: "assets/img/gallery/heatmap_tool.webp",
    link: "https://www.nytimes.com/2024/12/20/technology/connected-cars-roads-data.html",
    highlight: true
  },

  // ==========================================
  // 2023
  // ==========================================
  {
    id: "purdue-phd-2023",
    year: 2023,
    date: "May 2023",
    category: "awards",
    badge: "Ph.D. Hooding Ceremony",
    event: "Purdue University Doctoral Commencement",
    location: "West Lafayette, IN",
    caption: "Doctoral hooding ceremony at Elliott Hall of Music, conferral of Ph.D. in Civil Engineering for research on connected vehicle data for operational decision-making.",
    people: ["Prof. Darcy M. Bullock (Doctoral Advisor)", "Purdue Engineering Faculty"],
    image: "assets/img/gallery/purdue_phd_hooding_2023.png",
    link: "https://doi.org/10.25394/PGS.22684822.v1",
    highlight: true
  },
  {
    id: "trb-2023-weather-lectern",
    year: 2023,
    date: "January 2023",
    category: "podium",
    badge: "Lectern Session",
    event: "TRB 102nd Annual Meeting · Session 19287",
    location: "Washington, D.C.",
    caption: "Presenting research on the impact of rain intensity on interstate traffic speeds combining connected vehicle probe data with Doppler weather radar.",
    people: ["Dr. Haothian Li", "Dr. Darcy Bullock", "FHWA Road Weather Management Committee"],
    image: "assets/img/gallery/purdue_cv_field_deployment.jpg",
    link: "https://annualmeeting.mytrb.org/OnlineProgramArchive/Details/19287",
    highlight: true
  },
  {
    id: "road-school-2023-uas",
    year: 2023,
    date: "March 2023",
    category: "podium",
    badge: "Lectern Session",
    event: "109th Purdue Road School · Session 182",
    location: "West Lafayette, IN",
    caption: "Presenting work zone traffic monitoring methodology integrating connected vehicle speed profiles with unmanned aerial system (UAS) high-resolution video.",
    people: ["Dr. Jairaj Desai", "INDOT Work Zone Field Staff"],
    image: "assets/img/gallery/indiana_segment_pm.webp",
    highlight: true
  },
  {
    id: "purdue-ite-seminar-2023",
    year: 2023,
    date: "April 2023",
    category: "workshop",
    badge: "Campus Seminar",
    event: "Purdue ITE Weekly Seminar Series",
    location: "West Lafayette, IN",
    caption: "Invited research talk on evaluating precipitation impact on freeway operations utilizing Multi-Radar Multi-Sensor (MRMS) data.",
    people: ["Purdue ITE Student Chapter"],
    image: null,
    highlight: true
  },

  // ==========================================
  // 2022 & Prior
  // ==========================================
  {
    id: "its-midwest-2021",
    year: 2022,
    date: "November 2021",
    category: "awards",
    badge: "Project of the Year",
    event: "ITS Midwest Annual Meeting",
    location: "Chicago, IL",
    caption: "Honored with the 2021 ITS Midwest Project of the Year Award for evaluating queue trucks with navigation alerts using connected vehicle trajectory data.",
    people: ["INDOT Leadership", "ITS Midwest Board", "Dr. Darcy Bullock", "Dr. Jairaj Desai"],
    image: "assets/img/gallery/jtrp_research_portrait.jpg",
    link: "https://doi.org/10.4236/jtts.2021.114035",
    highlight: true
  },
  {
    id: "cricket-championship-2022",
    year: 2022,
    date: "October 2022",
    category: "awards",
    badge: "Championship Captain",
    event: "NCAA Midwest T-20 Cricket Championship",
    location: "Midwest",
    caption: "Captaining the Purdue University Cricket Club to the 2022 Midwest T-20 Championship trophy.",
    people: ["Purdue Cricket Club Championship Squad"],
    image: null,
    link: "https://www.purduecricket.com/",
    highlight: true
  },
  {
    id: "sparc-workshop-2021",
    year: 2021,
    date: "2021",
    category: "workshop",
    badge: "International Course Instructor",
    event: "Government of India SPARC Mobility Initiative",
    location: "Virtual / International",
    caption: "Developed curriculum and instructed three session modules on connected vehicle telematics and traffic performance measures for international scholars.",
    people: ["IIT Madras & Purdue SPARC Collaborative Faculty"],
    image: "assets/img/gallery/heatmap_tool.webp",
    highlight: true
  },
  {
    id: "trb-2022-queue-trucks",
    year: 2022,
    date: "January 2022",
    category: "poster",
    badge: "Poster Presentation",
    event: "TRB 101st Annual Meeting · Session 17526",
    location: "Washington, D.C.",
    caption: "Poster presentation evaluating queue warning trucks equipped with digital in-cab navigation alerts deployed across Indiana highway work zones.",
    people: ["Joshua McGregor", "Michelle Kachler", "Dr. Darcy Bullock"],
    image: null,
    highlight: true
  }
];
