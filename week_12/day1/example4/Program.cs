namespace trackProgram {

    class Track
    {
        private double _heading; // private field — guarded
        public int Id { get; } // read-only after construction
        public double Speed { get; set; }
        public double Heading // property with validation
        {
            get => _heading;
            set
            {
                if (value < 0 || value > 359)
                    _heading = 0; // correct an invalid value at the gate
                else
                    _heading = value;

            }
        }
        public Track(int id, double speed, double heading)
        {
            Id = id;
            Speed = speed;
            Heading = heading; // goes through the validating setter
        }
        public override string ToString() // the object prints itself
        => $"Track {Id}: {Speed} kn, heading {Heading}";

    }

    class program
    {
        static void Main()
        {
            Track t = new Track(17, 412.5, 270);
            Console.WriteLine(t); // ToString() is called automatically
            //t.Heading = 999; // invalid
            //Console.WriteLine(t.Heading); // 0 — the setter corrected it
            t.Speed = 99;
            Console.WriteLine(t); // ToString() is called automatically

        }
}

}