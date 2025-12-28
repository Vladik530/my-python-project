using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace zadanie2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            uint n;
            do
            {
                Console.WriteLine("----Menu----");
                Console.WriteLine("1-zadanie\n2-zadanie\n3-zadanie\n4-koniec");
                Console.Write("Wybierz opcje:");
                n = uint.Parse(Console.ReadLine());
                switch (n)
                {
                    case 1:
                        Zadanie1();
                        break;
                    case 2:
                        Zadanie2();
                        break;
                    case 3:
                        Zadanie3();
                        break;
                    case 4:
                        Console.WriteLine("Dziekujemy za program");
                        break;
                    default:
                        Console.WriteLine("Nie ma takiej opcji!!!");
                        break;
                }
            }
            while (n != 4);
        }
        static void Zadanie1()
        {
            uint t;
            Console.WriteLine("Podaj wiek:");
            t = uint.Parse(Console.ReadLine());
            if(t < 18)
            {
                Console.WriteLine("Jesteś niepelnoletni");
            }
            else
            {
                Console.WriteLine("Jesteś pelnoletni");
            }
        }
        static void Zadanie2()
        {
            uint n;
            Console.Write("Podaj liczbe:");
            n = uint.Parse(Console.ReadLine());
            int[] d = new int[n];
            
            for(int i = 0; i < d.Length; i++)
            {
                Console.WriteLine(i);
            }
            Console.WriteLine();
            for (int i = 0; i < d.Length; i+=2)
            {
                Console.WriteLine(i);
            }
            Console.WriteLine();
            for (int i = 20; i > d.Length; i --)
            {
                Console.WriteLine(i);
            }
            Console.WriteLine();
            for (int i = 20; i > d.Length; i-=2)
            {
                Console.WriteLine(i);
            }
        }
        static void Zadanie3()
        {
            uint y;
            Random r = new Random();
            int propa = r.Next(0, 10);
            int limit = 0;
           
                do
                {
                    Console.Write("Podaj liczbę:");
                    y = uint.Parse(Console.ReadLine());
                    if (y > 10)
                    {
                        Console.WriteLine("Liczba nie może być więcej niż 10");
                    }
                    else if (y == propa)
                    {
                        Console.WriteLine("Wy zgadneli liczbę");
                    }
                    else
                    {
                        Console.WriteLine("Wy nie gdadneli liczbę");
                    }
                } while (y != propa && limit < 6);
            
                    
            
        }
    }
}
