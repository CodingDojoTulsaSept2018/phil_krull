using System;

namespace Phone
{
    public class Galaxy : Phone, IRingable 
    {
        public Galaxy(string versionNumber, int batteryPercentage, string carrier, string ringTone) : base(versionNumber, batteryPercentage, carrier, ringTone) {}
        public string Ring() 
        {
            // your code here
            return $"........ { RingTone } ..........";
        }
        public string Unlock() 
        {
            // your code here
            return $"Galaxy { VersionNumber } unlocked with fingerprint scanner";
        }
        public override void DisplayInfo() 
        {
            // your code here            
            Console.WriteLine("##############################");
            Console.WriteLine($"Galaxy { VersionNumber }");
            Console.WriteLine($"Batter Percentage: { BatteryPercentage }");
            Console.WriteLine($"Carrier: { Carrier }");
            Console.WriteLine($"Ring Tone: { RingTone }");
            System.Console.WriteLine("##############################");
        }
    }
}
