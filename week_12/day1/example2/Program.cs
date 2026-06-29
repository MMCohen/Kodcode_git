// Track t = new Track(); // <- now this FAILS to compile
Track t = new Track(17); // you must use the one you wrote
class Track
{
    public int Id;

    public Track(int id) { 
        Id = id;
        Console.WriteLine("costorotor run");
    }
}



