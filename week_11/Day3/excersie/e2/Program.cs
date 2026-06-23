static bool FindSpeed(string id, out double speed)
{
    speed = 0; // out parameters must be set before returning
if (id == "TR-1") { speed = 420.5; return true; }
    return false;
}
//if (FindSpeed("TR1", out double s))
//    Console.WriteLine($"found: {s}"); // found: 420.5

//else
//    Console.WriteLine($"{s} not found");

FindSpeed("TR-1", out double _);