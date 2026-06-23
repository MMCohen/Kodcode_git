using System;
using System.Dynamic;

namespace IntelSource
{

    enum ClassificationType{Friendly, Hostile, Unidentified}


    class SignalInterceptLog
    {

        //int x = "hello";


        static void Create(List<int> sourceId, List<ClassificationType> classType, List<double?> signalStrength)
        {
            Console.WriteLine("hello from create");

            int UserIntId = GetSourceID();
            ClassificationType userClassification = GetClassification();
            double? userStrength = GetStrength();

            sourceId.Add(UserIntId);
            classType.Add(userClassification);
            signalStrength.Add(userStrength);
        }


        static int GetSourceID()
        {
            Console.Write("Please enter id [int only]: ");
            string userID = Console.ReadLine();

            int intId;

            while (!int.TryParse(userID, out intId))
            {
                Console.Write("Please enter id [int only]: ");
                userID = Console.ReadLine();
            }

            return intId;
        }


        static ClassificationType GetClassification()
        {
            Console.Write("Please enter classification [Friendly, Hostile, Unidentifiedy]: ");
            string userClass = Console.ReadLine();

            ClassificationType classification;

            while (!ClassificationType.TryParse(userClass, out classification))
            {
                Console.Write("Please enter classification [Friendly, Hostile, Unidentifiedy]: ");
                userClass = Console.ReadLine();
            }

            return classification;
        }


        static double? GetStrength()
        {
            bool notDouble = true;
            double? strength;

            while (notDouble)
            {
                Console.WriteLine("Please enter strength [empty/double]; ");
                string? userStrength = Console.ReadLine();

                if (userStrength == null)
                {
                    return null;
                }

                else if (double.TryParse(userStrength, out double tempStrength))
                {
                    strength = tempStrength;
                    notDouble = false;
                }
            return strength;
            }
        }


        static void editStrength()
        {
            return;
        }


        static void Main()
        {
            List<int> SourceId = new();
            List<ClassificationType> Classification = new();
            List<double?> SignalStrength = new();

            Console.WriteLine("Hello from main");

            
        }
    }
}