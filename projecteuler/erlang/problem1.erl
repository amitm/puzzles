#!/usr/local/bin/escript
main(_) ->
    Useable = fun(X) when X rem 3 =:= 0; X rem 5 =:= 0 -> X;
    	         (_) -> 0
    	      end,
    For = fun(_, 1000, N) -> N;
    		 (For, I, N) -> For(For, I + 1, N + Useable(I))
    	  end,
    io:format("~w\n", [For(For, 1, 0)]).
