alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,false), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), le(P,rec_afp,235), le(P,don_microesteatosis,50).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,false), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,184,235), le(P,don_microesteatosis,50), le(P,rec_provenance,50).
not_alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,false), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,184,235), le(P,don_microesteatosis,50), gt(P,rec_provenance,50).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,false), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,235,495), le(P,don_microesteatosis,50), le(P,rec_provenance,150).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,false), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), gt(P,rec_afp,235), le(P,don_microesteatosis,50), le(P,rec_provenance,150).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,false), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), gt(P,rec_afp,235), le(P,don_microesteatosis,50), between(P,rec_provenance,50,150).
not_alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,false), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), gt(P,rec_afp,235), le(P,don_microesteatosis,50), gt(P,rec_provenance,150).
alive(P) :- holds(P,rec_abdominal_surgery,true), holds(P,don_acv,false), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), le(P,don_microesteatosis,50).
alive(P) :- holds(P,don_acv,false), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), gt(P,don_microesteatosis,50).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), le(P,rec_afp,385), le(P,don_microesteatosis,50), le(P,rec_provenance,100).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), le(P,rec_afp,385), le(P,don_microesteatosis,50), gt(P,rec_provenance,100).
alive(P) :- holds(P,rec_abdominal_surgery,true), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), le(P,rec_afp,385), le(P,don_microesteatosis,50).
not_alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,254,385), le(P,don_microesteatosis,50), le(P,rec_provenance,50).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,254,385), le(P,don_microesteatosis,50), gt(P,rec_provenance,50).
not_alive(P) :- holds(P,rec_abdominal_surgery,true), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,254,385), le(P,don_microesteatosis,50).
alive(P) :- holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), le(P,rec_afp,385), gt(P,don_microesteatosis,50).
not_alive(P) :- holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,270,385), gt(P,don_microesteatosis,50).
alive(P) :- holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,304,385).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,385,30825), le(P,don_microesteatosis,100), le(P,rec_provenance,50).
not_alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,385,30825), gt(P,don_microesteatosis,100), le(P,rec_provenance,50).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,385,30825), le(P,rec_provenance,50).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,385,30825), le(P,don_microesteatosis,100), gt(P,rec_provenance,50).
not_alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,385,30825), gt(P,don_microesteatosis,100), gt(P,rec_provenance,50).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,385,30825), gt(P,rec_provenance,50).
not_alive(P) :- holds(P,rec_abdominal_surgery,true), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,385,30825).
alive(P) :- holds(P,rec_abdominal_surgery,true), holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), between(P,rec_afp,385,30825).
not_alive(P) :- holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_hypertension,false), gt(P,rec_afp,385).
alive(P) :- holds(P,don_acv,false), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), le(P,rec_afp,1244).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), le(P,rec_afp,1244), le(P,don_microesteatosis,50).
not_alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), between(P,rec_afp,509,1244), le(P,don_microesteatosis,50).
not_alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), le(P,rec_afp,1244), gt(P,don_microesteatosis,50).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,don_acv,true), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), between(P,rec_afp,634,1244).
alive(P) :- holds(P,rec_abdominal_surgery,true), holds(P,don_acv,true), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), le(P,rec_afp,1244).
not_alive(P) :- holds(P,don_acv,false), holds(P,rec_abdominal_surgery,false), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), between(P,rec_afp,1244,21450), le(P,don_microesteatosis,100).
alive(P) :- holds(P,don_acv,false), holds(P,rec_abdominal_surgery,false), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), between(P,rec_afp,1244,21450), le(P,don_microesteatosis,100).
not_alive(P) :- holds(P,don_acv,true), holds(P,rec_abdominal_surgery,false), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), between(P,rec_afp,1244,21450), le(P,don_microesteatosis,100).
not_alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), between(P,rec_afp,1244,21450), le(P,don_microesteatosis,100).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), gt(P,rec_afp,1244), le(P,don_microesteatosis,100).
not_alive(P) :- holds(P,don_acv,false), holds(P,rec_abdominal_surgery,false), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), gt(P,rec_afp,1244), gt(P,don_microesteatosis,100).
alive(P) :- holds(P,don_acv,true), holds(P,rec_abdominal_surgery,false), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), gt(P,rec_afp,1244), gt(P,don_microesteatosis,100).
not_alive(P) :- holds(P,rec_abdominal_surgery,true), holds(P,rec_vhc,true), holds(P,rec_hypertension,false), gt(P,rec_afp,1244).
alive(P) :- holds(P,rec_vhc,false), holds(P,rec_abdominal_surgery,false), holds(P,rec_hypertension,true), le(P,rec_afp,20994), le(P,don_microesteatosis,50), le(P,rec_provenance,100).
alive(P) :- holds(P,don_acv,false), holds(P,rec_vhc,false), holds(P,rec_abdominal_surgery,false), holds(P,rec_hypertension,true), between(P,rec_afp,479,20994), le(P,don_microesteatosis,50), le(P,rec_provenance,100).
alive(P) :- holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_abdominal_surgery,false), holds(P,rec_hypertension,true), between(P,rec_afp,479,20994), le(P,don_microesteatosis,50), le(P,rec_provenance,100).
alive(P) :- holds(P,don_acv,true), holds(P,rec_vhc,false), holds(P,rec_abdominal_surgery,false), holds(P,rec_hypertension,true), between(P,rec_afp,479,20994), le(P,don_microesteatosis,50), le(P,rec_provenance,100).
alive(P) :- holds(P,rec_vhc,false), holds(P,rec_abdominal_surgery,false), holds(P,rec_hypertension,true), le(P,rec_afp,20994), le(P,don_microesteatosis,50), gt(P,rec_provenance,100).
alive(P) :- holds(P,rec_vhc,true), holds(P,rec_abdominal_surgery,false), holds(P,rec_hypertension,true), le(P,rec_afp,20994), le(P,don_microesteatosis,50).
alive(P) :- holds(P,don_acv,false), holds(P,rec_vhc,true), holds(P,rec_abdominal_surgery,false), holds(P,rec_hypertension,true), between(P,rec_afp,915,20994), le(P,don_microesteatosis,50).
not_alive(P) :- holds(P,don_acv,true), holds(P,rec_vhc,true), holds(P,rec_abdominal_surgery,false), holds(P,rec_hypertension,true), between(P,rec_afp,915,20994), le(P,don_microesteatosis,50).
alive(P) :- holds(P,don_acv,true), holds(P,rec_vhc,true), holds(P,rec_abdominal_surgery,false), holds(P,rec_hypertension,true), between(P,rec_afp,915,20994), le(P,don_microesteatosis,50).
not_alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,rec_hypertension,true), gt(P,rec_afp,20994), le(P,don_microesteatosis,50).
alive(P) :- holds(P,rec_abdominal_surgery,false), holds(P,rec_hypertension,true), gt(P,don_microesteatosis,50).
not_alive(P) :- holds(P,rec_abdominal_surgery,true), holds(P,rec_hypertension,true), le(P,rec_afp,134).
alive(P) :- holds(P,rec_abdominal_surgery,true), holds(P,rec_hypertension,true), gt(P,rec_afp,134).

%!trace {"% is true",F} holds(P,F,true).
%!trace {"% is false",F} holds(P,F,false). 

%!trace {"% > %", F, T} gt(P,F,T).
%!trace {"% <= %", F, T} le(P,F,T).
%!trace {"% in (%,%]", F, Min, Max} between(P,F,Min,Max).