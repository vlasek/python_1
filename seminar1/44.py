# *4. Найти точку пересечения двух прямых заданных уравнением y=kx+b, 
# /а1 k1 и а2 и k2 заданы


a1=3
a2=2
k1=2
k2=3
double y1, y2;
double e=1E-10;
double start=-10;
double finish=10;
double dx=(finish-start)/10000;


for (x x<=finish; x=x+dx)
{
    y1=a1*x+k1;
    y2=a2*x+k2;
    if (Math.Abs(y1-y2)<=e) {Console.WriteLine($"Значение {y1} и {x}");break;}
    
}
