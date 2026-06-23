static void TryDouble(int n) { n = n * 2; } // n is a copy
static void AddOne(List<int> xs) { xs.Add(1); } // xs points to the same list
int x = 10;
TryDouble(x);
Console.WriteLine(x); // 10 — the int was copied, caller unchanged
List<int> list = new List<int>();
AddOne(list);
Console.WriteLine(list.Count); // 1 — the list is shared, caller sees the change