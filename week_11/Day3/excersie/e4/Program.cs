double? speed = null; // radar has not locked — truly unknown
Console.WriteLine(speed.HasValue); // False
Console.WriteLine(speed ?? -1); // -1 stands in for unknown whenprinting
speed = 412.5; // now the radar locked
Console.WriteLine(speed.HasValue); // True
Console.WriteLine(speed.Value); // 412.5