tools = {
    "general_hand_tools": [
        "box wrench", "socket",
        "screwdriver", "torx screwdriver", "screwdriver (hex)", "socket wrench",
        "pliers", "pliers",
        "rubber mallet", "claw hammer", "hammer", "ratchet", "socket set",
        "torque wrench", "pry bar", "utility knife", "measuring tape", "Allen keys (hex keys)", "O-ring", 
        "strainer", "cup", "wrench", "stopper", "screw", "screws", "gauge"
    ],
    "automotive_tools": [
        "drain pan", "spark plug wrench", "oil filter wrench", "brake bleeder kit", "tire pressure gauge",
        "hydraulic jack", "scissor jack", "jack stands", "lug wrench", "funnel", "battery tester",
        "timing light", "compression tester", "valve spring compressor", "feeler gauge",
        "coolant tester", "exhaust gas analyzer", "chain breaker tool", "carburetor synchronizer",
        "chain alignment tool", "pad spreader",
    ],
    "electrical_tools": [
        "multimeter", "wire stripper", "crimping tool", "heat gun", "soldering iron",
        "circuit tester", "electrical tape", "fuses", "battery charger"
    ],
    "diagnostic_tools": [
        "scanner", "diagnostic software", "fuel pressure gauge", "manometer"
    ],
    "body_repair_tools": [
        "sandpaper", "body filler applicator", "spray gun", "dent puller",
        "panel removal tools", "trim removal tools"
    ],
    "printer_specific_tools": [
        "anti-static gloves", "tweezers", "precision screwdriver set",
        "cleaning solution", "cotton swabs", "lint-free cloth", "ink cartridge reset tool",
        "calibration tool", "belt tensioning tool", "printer alignment sheets"
    ],
    "specialized_tools": [
        "flywheel puller", "torque angle gauge", "piston ring compressor", "bearing puller",
        "dial indicator", "micrometer", "vernier caliper", "chain alignment laser", "oil syringe",
        "snap ring pliers"
    ],
    "cleaning_tools": [
        "parts washer", "brake cleaner", "degreaser", "compressed air can",
        "shop towels", "wire brush"
    ],
    "safety_equipment": [
        "safety glasses", "mechanics gloves", "hearing protection", "fire extinguisher",
        "respirator mask", "applicator"
    ],
    "miscellaneous_supplies": [
        "zip ties", "rubber O-rings", "gaskets", "sealant",
        "lubricants", "replacement bulbs", "hose clamps"
    ]
}

# To access all tools as a flat list:
all_tools = [tool for category in tools.values() for tool in category]
print(all_tools)
