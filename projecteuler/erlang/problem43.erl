#!/usr/local/bin/escript
main(_) ->
	NumberSet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
	Divisors = [13, 11, 7, 5, 3, 2],
	Numbers = lists:map(fun(X) when length(X) =:= 3 -> X; (X) -> [0|X] end, 
						[lists:map(fun(Y) -> Y - 48 end, integer_to_list(X * 17)) || X <- lists:seq(1,58)]),
	_UniqueHelper = fun(_, _, _, 2) -> false;
					   (_, _, [], _) -> true;
					   (_UniqueHelper, Number, [Number|T], Count) -> _UniqueHelper(_UniqueHelper, Number, T, Count + 1);
					   (_UniqueHelper, Number, [_|T], Count) -> _UniqueHelper(_UniqueHelper, Number, T, Count)          
			 		end,
	Unique = fun(List) -> _UniqueHelper(_UniqueHelper, lists:nth(1, List), List, 0) and
  						  _UniqueHelper(_UniqueHelper, lists:nth(2, List), List, 0) and
						  _UniqueHelper(_UniqueHelper, lists:nth(3, List), List, 0) 
			 end,
	Divisible = fun(Number, Divisor) -> (100 * lists:nth(1, Number) + 
										10 * lists:nth(2, Number) + 
										1 * lists:nth(3, Number)) rem Divisor =:= 0
				end,
	ToInteger = fun(X) -> list_to_integer(lists:map(fun(Y) -> Y + 48 end, X)) end,
	GetSpecialSum = fun(_, Number, [H|[]], _) -> ToInteger([H|Number]);
					   (Helper, Number, NumSet, Divs) -> lists:sum(lists:map(fun(X) -> Helper(Helper,
																							  [X|Number], 
																							  NumSet -- [X],
																							  Divs)
																			 end, 
																	 		 NumSet))
					end,
	GetSpecialSumHelperHelper = fun(Helper, Number, NumSet, List, true) -> GetSpecialSum(Helper, Number, NumSet, List);
							       (_, _, _, _, _) -> 0
							    end,
	GetSpecialSumHelper = fun(GetSpecialSumHelper, Number, NumSet, [Divisor|T]) -> GetSpecialSumHelperHelper(GetSpecialSumHelper, Number, NumSet, T, Divisible(Number, Divisor)) end,
	io:format("~w\n", [lists:sum(lists:map(fun(X) -> GetSpecialSum(GetSpecialSumHelper, X, NumberSet -- X, Divisors) end, [X || X <- Numbers, Unique(X)]))]).
	


