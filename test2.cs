using System;

class Program
{
    static void Main()
    {
        Console.Write("Podaj pierwszą liczbę: ");
        double a = Convert.ToDouble(Console.ReadLine());

        Console.Write("Podaj działanie (+, -, *, /): ");
        string dzialanie = Console.ReadLine();

        Console.Write("Podaj drugą liczbę: ");
        double b = Convert.ToDouble(Console.ReadLine());

        double wynik;

        switch (dzialanie)
        {
            case "+":
                wynik = a + b;
                break;

            case "-":
                wynik = a - b;
                break;

            case "*":
                wynik = a * b;
                break;

            case "/":
                if (b == 0)
                {
                    Console.WriteLine("Nie można dzielić przez zero!");
                    return;
                }

                wynik = a / b;
                break;

            default:
                Console.WriteLine("Nieprawidłowe działanie!");
                return;
        }

        Console.WriteLine($"Wynik: {wynik}");
    }
}
