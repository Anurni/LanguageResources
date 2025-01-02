tools = {
    "general_hand_tools": [
         "screwdriver", "screwdriver (Torx)", "screwdriver (hex)",
        "wrench (adjustable)", "wrench (box-end)", "wrench (combination)", "socket wrench",
        "pliers (needle-nose)", "pliers (cutting)", "pliers (slip-joint)", "pliers (locking)",
        "rubber mallet", "claw hammer", "ball-peen hammer", "ratchet", "socket set",
        "torque wrench", "pry bar", "utility knife", "measuring tape", "Allen keys (hex keys)", "O-ring", 
        "strainer", "cup", "wrench"
    ],
    "automotive_tools": [
        "spark plug wrench", "oil filter wrench", "brake bleeder kit", "tire pressure gauge",
        "hydraulic jack", "scissor jack", "jack stands", "lug wrench", "funnel", "battery tester",
        "timing light", "compression tester", "valve spring compressor", "feeler gauge",
        "coolant tester", "exhaust gas analyzer", "chain breaker tool", "carburetor synchronizer",
        "chain alignment tool", "brake pad spreader", "fuel valve", "fuel cup", 
    ],
    "electrical_tools": [
        "multimeter", "wire stripper", "crimping tool", "heat gun", "soldering iron",
        "circuit tester", "electrical tape", "fuses", "battery charger"
    ],
    "diagnostic_tools": [
        "OBD-II scanner", "diagnostic software", "fuel pressure gauge", "manometer"
    ],
    "body_repair_tools": [
        "sandpaper", "body filler applicator", "spray gun", "dent puller",
        "panel removal tools", "trim removal tools"
    ],
    "printer_specific_tools": [
        "anti-static gloves", "tweezers", "precision screwdriver set",
        "cleaning solution", "cotton swabs", "lint-free cloth", "ink cartridge reset tool",
        "calibration tools/software", "belt tensioning tool", "printer alignment sheets"
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
        "respirator mask"
    ],
    "miscellaneous_supplies": [
        "zip ties", "rubber O-rings", "gaskets", "sealant (e.g., RTV, thread lock)",
        "lubricants (grease, WD-40, chain lube)", "replacement bulbs", "hose clamps", "container"
    ]
}

# To access all tools as a flat list:
all_tools = [tool for category in tools.values() for tool in category]
print(all_tools)
