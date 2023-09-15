%!trace {"% > %_t", FName, T} gt(I,F,T) : feature_name(F,FName).
%!trace {"% <= %_t", FName, T} le(I,F,T) : feature_name(F,FName).
%!trace {"% in (%_t,%_t]", FName, Min, Max} between(I,F,Min,Max) : feature_name(F,FName).

%!trace {"feature % > %_t", F, T} gt(I,F,T) : not feature_names.
%!trace {"feature % <= %_t", F, T} le(I,F,T) : not feature_names.
%!trace {"feature % in (%_t,%_t]", F, Min, Max} between(I,F,Min,Max) : not feature_names.

feature_names :- feature_name(F,FName).
