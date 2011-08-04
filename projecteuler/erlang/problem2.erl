#!/usr/local/bin/escript
main(_) ->
    Fib = fun(_, {_, Y}, Total) when Y >= 4000000 -> Total;
             (Fib, {X, Y}, Total) when Y rem 2 =:= 0 -> Fib(Fib, {Y, X + Y}, Y + Total);
             (Fib, {X, Y}, Total) -> Fib(Fib, {Y, X + Y}, Total)
          end,
    io:format("~w\n", [Fib(Fib, {1, 2}, 0)]).
