module Cartas_Inglesas where

type ValorN = String
type Palo = String
type CartaI = (Palo, ValorN)
type CartasI = [CartaI]

barajaN::CartasI
barajaN = [("trebloes","A"),("treboles","2"),("treboles","3"),("diamantes","4"),("diamantes","5"),("diamantes","6"),("corazones","7"),("corazones","8"),("corazones","9"),("picas","10"),("picas","J"),("picas","Q")]

buscar::CartasI->CartaI->Bool
buscar [] cartai = False
buscar ((x,y): ci) (palo,valorN)
    | x == palo && y == valorN = True
    | otherwise = buscar ci (palo,valorN)
valor_R::CartaI->String
valor_R (palo,valorN)
    | valorN == "A" = "1"
    | valorN == "j" = "11"
    | valorN == "Q" = "12"
    | valorN == "K" = "13"
