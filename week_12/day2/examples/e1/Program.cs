
/*
namespace example1
{
    class Track
    {
        public int Id { get; }
        public double Speed { get; set; }
        public Track(int id, double speed)
        {
            Id = id;
            Speed = speed;
            Console.WriteLine("hello from track constractor");
        }
    }
    class Aircraft : Track // Aircraft IS-A Track
    {
        public double Altitude { get; }
        public Aircraft(int id, double speed, double altitude)
        : base(id, speed) // build the Track part first
        {
            Console.WriteLine("hello from aircraft constractor");
            
            Altitude = altitude; // then the part unique to Aircraft
        }
    }

    class Program
    {
        static void Main()
        {
            Aircraft a = new Aircraft(1, 420, 30000);
            Console.WriteLine($"{a.Id} {a.Speed} {a.Altitude}"); // Id and Speed inherited
        }
    }
}


namespace example2
{
    class Track
    {
        public int Id { get; }
        public Track(int id) { Id = id; }
        public virtual string Describe() // virtual: a derived class MAY replace it
            => $"Track {Id}";
    }
    class Aircraft : Track
    {
        public double Altitude { get; }
        public Aircraft(int id, double altitude) : base(id)
        {
            Altitude = altitude;
        }
        public override string Describe() // override: this kind replaces the behavior
            => $"Aircraft {Id} at {Altitude} ft";
    }

    

}


namespace example3
{
    abstract class Track // abstract: a Track "in general" cannot exist
    {
        public int Id { get; }
        public double Speed { get; set; }
        protected Track(int id, double speed) // base constructor for derived classes
        {
            Id = id;
            Speed = speed;
        }
        public abstract string Describe(); // no body — every kind MUST implement it
    }

    class Aircraft : Track
    {
        public double Altitude { get; }
        public Aircraft(int id, double speed, double altitude)
        : base(id, speed) => Altitude = altitude;
        public override string Describe()
        => $"Aircraft {Id} at {Altitude} ft, {Speed} kn";
    }

    class Vessel : Track
    {
        public Vessel(int id, double speed) : base(id, speed) { }
        public override string Describe()
        => $"Vessel {Id}, {Speed} kn";
    }



    class Program
    {
        public static void Main()
        {
            // Track t = new Track(1, 100); // <- compile error: cannot create an abstract class
            //Severity Code Description Project File Line Suppression State
            //Error (active) CS0144 Cannot create an instance of the abstract type or
            //interface 'Track' W2D2 D:\C#Projects\W2D2\Program.cs 34

            Aircraft a = new Aircraft(1, 420, 30000); // concrete kinds are fine

            Console.WriteLine(a.Describe());
        }

    }

}

*/

namespace example4
{
    abstract class Track // abstract: a Track "in general" cannot exist
    {
        public int Id { get; }
        public double Speed { get; set; }
        protected Track(int id, double speed) // base constructor for derived classes
        {
            Id = id;
            Speed = speed;
        }
        public abstract string Describe(); // no body — every kind MUST implement it
    }

    class Aircraft : Track
    {
        public double Altitude { get; }
        public Aircraft(int id, double speed, double altitude)
        : base(id, speed) => Altitude = altitude;
        public override string Describe()
        => $"Aircraft {Id} at {Altitude} ft, {Speed} kn";
    }

    class Vessel : Track
    {
        public Vessel(int id, double speed) : base(id, speed) { }
        public override string Describe()
        => $"Vessel {Id}, {Speed} kn";
    }



    class Program
    {
        public static void Main()
        {
            Aircraft a = new Aircraft(1, 300, 30000); // concrete kinds are fine
            Vessel b = new Vessel(1, 300); // concrete kinds are fine

            Track[] allArr = new Track[3]; // arr of tracks holds different kinds of trcks
            allArr[0] = a;
            allArr[1] = b;
            allArr[2] = new Aircraft(1, 2, 3);

            for (int i = 0; i < allArr.Length; i++)
            {
                Console.WriteLine(allArr[i].Describe());
            }

            List<Track> all = new()
                    {
                        new Aircraft(1, 420, 30000),
                        new Vessel(2, 18),
                        new Aircraft(3, 510, 41000)
                    };
            foreach (Track t in all)
                Console.WriteLine(t.Describe()); // each object responds in its own way
        }

    }

}




