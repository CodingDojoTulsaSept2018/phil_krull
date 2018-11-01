using System;

namespace Phone
{
    public class Nokia : Phone, IRingable
    {
        public Nokia(string versionNumber, int batteryPercentage, string carrier, string ringTone) : base(versionNumber, batteryPercentage, carrier, ringTone) {}
        public string Ring()
        {
            // your code here
            return $"....... { RingTone } ..........";
        }
        public string Unlock()
        {
            // your code here
            return $"Nokia { VersionNumber } was unlocked with a passcode";
        }
        public override void DisplayInfo() 
        {
            // your code here
            Console.WriteLine("$$$$$$$$$$$$$$$$$$$$$$$$$");
            Console.WriteLine($"Nokia { VersionNumber }");
            Console.WriteLine($"Batter Percentage: { BatteryPercentage }");
            Console.WriteLine($"Carrier: { Carrier }");
            Console.WriteLine($"Ring Tone: { RingTone }");
            System.Console.WriteLine("$$$$$$$$$$$$$$$$$$$$$$$$$");
        }
    }
}