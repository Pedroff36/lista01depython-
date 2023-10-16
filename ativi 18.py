tamanho = float(input('Tamanho do arquivo (MB): ')) 
velocidade=float(input('velocidade da internet (mbps)'))
print('Tempo aproximado de download: %.0f Minutos ' %((tamanho / velocidade) * 60))
	