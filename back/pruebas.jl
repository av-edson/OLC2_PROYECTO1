# function rec_fib(n)
#     if n > 1
#         return rec_fib(n-1) + rec_fib(n-2);
#     else
#         return n;
#     end;
# end;
# println(rec_fib(10));

# function cuenta_regresiva(numero)
#     numero =numero- 1
#     if numero > 0
#         println(numero);
#         cuenta_regresiva(numero);
#     else
#         println("Boooooooom!");
#     end;
#     println("Fin de la función", numero);
# end;
# cuenta_regresiva(5);

#function factorial(numero)
#    println("Valor inicial ->",numero);
#    if numero > 1
#        numero = numero * factorial(numero -1);
#    end;
#    println("valor final ->",numero);
#    return numero;
#end;
#println(factorial(5));

function ackerman(m::Int64,n::Int64)
    if( (n<0) || (m<0) )
        println("Parametros no validos");
    end;
    if(m==0)
        return (n+1);
    end;
    if(n==0)
        a = ackerman(m-1,1)
        return a;
    end;
    b = ackerman(m-1,ackerman(m,n-1));
    return b;
end;

a=ackerman(2,4);
print(a);