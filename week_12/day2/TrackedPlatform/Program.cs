
namespace TrackPlatform
{
    abstract class Platform
    {
        private int _trackId { get; }
        private double _speedKnots { get; set; }
        private double _heading { get; set; }

        protected int TrackId { get => _trackId; }
        protected double SpeedKnots
        {
            get => _speedKnots;
            set
            {
                if (value < 0) { _speedKnots = 0; }
                else { _speedKnots = value; }
            }
        }
        protected double Heading
        {
            get => _heading;
            set
            {
                if (value < 0 || value > 359) {_heading = 0;}
                else _heading = value;
            }
        }


        public abstract string StatusLine();
        public abstract bool IsTrackable();

        public override string ToString()
        {
            return $"Track id: {_trackId}. SpeedKnots: {_speedKnots}. Heading: {_heading}";
        }

        protected Platform(int trackId, double speedknots, double heading)
        {
            _trackId = trackId;
            SpeedKnots = speedknots;
            Heading = heading;
        }
    }


    class AirPlatform : Platform
    {
        private double _altitudeFeet;

        public override string StatusLine()
            => $"== AirPlatform == TrackID: {TrackId} | SpeedKnots: {SpeedKnots} | Heading: {Heading} | AltitudeFeet: {_altitudeFeet}";
        public override bool IsTrackable()
            => _altitudeFeet >= 100 && _altitudeFeet <= 60000 && SpeedKnots > 0;

        public AirPlatform(int trackId, double speedknots, double heading, double altitudefeet)
            : base(trackId, speedknots, heading)
        {
            _altitudeFeet = altitudefeet; // TODO: does it must be positive
        }

    }

    class SeaPlatform : Platform
    {
        private double _depthMeters;

        public override string StatusLine()
            => $"== SeaPlatform == TrackID: {TrackId} | SpeedKnots: {SpeedKnots} | Heading: {Heading} | DepthMeters: {_depthMeters}";

        public override bool IsTrackable()
            => _depthMeters >= 0 && _depthMeters <= 300;

        public SeaPlatform(int trackId, double speedknots, double heading, double depthmeters)
            : base(trackId, speedknots, heading) { _depthMeters = depthmeters; }
    }

    class GroundPlatform : Platform
    {
        private string _terrainType;

        public override string StatusLine()
            => $"== GroundPlatform == TrackID: {TrackId} | SpeedKnots: {SpeedKnots} | Heading: {Heading} | TerrainType: {_terrainType}";


        public override bool IsTrackable()
            => _terrainType.ToLower() != "tunnel";

        public GroundPlatform(int trackId, double speedknots, double heading, string terraintype)
            : base(trackId, speedknots, heading) { _terrainType = terraintype; }
    }

    class Program
    {
        static void Main()
        {
            List<Platform> platformList = new();

            AirPlatform ap1 = new AirPlatform(1, 400, 280, 20350);
            AirPlatform ap2 = new AirPlatform(2, 9, 280, 70000);
            SeaPlatform sp1 = new SeaPlatform(3, 70, 25, 150);
            SeaPlatform sp2 = new SeaPlatform(4, 3, 3, 400);
            GroundPlatform g1 = new GroundPlatform(5, 3, 3, "we4re");
            GroundPlatform g2 = new GroundPlatform(6, 3, 3, "we4re");

            platformList.Add(ap1);
            platformList.Add(ap2);
            platformList.Add(sp1);
            platformList.Add(sp2);
            platformList.Add(g1);
            platformList.Add(g2);

            foreach (Platform p in platformList) { Console.WriteLine(p.StatusLine() + " | IsTruckable: " + p.IsTrackable()); ; }

        }
    }

}