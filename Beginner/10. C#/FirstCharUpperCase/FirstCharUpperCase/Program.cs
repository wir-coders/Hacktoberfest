using System;

namespace FirstCharUpperCase
{
    class Program
    {
        static void Main(string[] args)
        {
            string sentence = "its a bright sunny day.";
            Program p = new Program();
            Console.WriteLine("Sentence before formatting is - {0}",sentence);
            sentence = p.UpperCase(sentence);
            Console.WriteLine("Sentence with 1st character as upper case is - {0}", sentence);
            Console.ReadKey();
        }

        public string UpperCase(string sentence)
        {
            return char.ToUpper(sentence[0]) + sentence.Substring(1);

        }
    }
}
