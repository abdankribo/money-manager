package money
type Transaction struct{Amount float64; Income bool}
func Balance(v []Transaction)float64{b:=0.0;for _,t:=range v{if t.Income{b+=t.Amount}else{b-=t.Amount}};return b}
