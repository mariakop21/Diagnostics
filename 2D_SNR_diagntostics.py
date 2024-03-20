import numpy as np
import argparse

############################################### 2-dimensional diagnostics ##############################################
# This code checks if a source is a candidate Supernova Remnnant (SNR) or not, 
# based on 2D diagnostics developed by Kopsacheili M. et al, 2020, MNRAS, 491, 889.
# One should run: 
# python 2D_SNR_diagntostics.py -ha [x1] -sii [x2] -nii [x3]  -oi [x4] -oii [x5] -oiii [x6] -hb [x7] -diag [diagntostic]
# where [x1], [x2], ..... [x7] is the observed flux/luminosity of a source  of:
# Hα(6563), [S II](6717,6731), [N II](6583), [O I](6300), [O II](3729,3731), [O III](5007), Hβ(4681) respectively.
# The parameter 'diag' refers to the diagnostics and it should be one of the following:
# 1.'SII-NII', 2.'NII-OIII', 3.'SII-OIII', 4.'OI-OIII', 5.'NII-OI', 
# 6.'OII-OIII', 7.'NII-OII', 8.'SII-OI', 9.'OI-OII', 10.'SII-OII'
# Those are the diagntostics that combine the emission line ratios: 
# 1.[S II]/Ha-[N II]/Ha,  2.[N II]/Ha-[O III]/Hb, 3.[S II]/Ha-[O III]/Hb, 4.[O I]/Ha-[O III]/Hb, 5. [N II]/Ha-[O I]/Ha
# 6.[O II]/Hb-[O III]/Hb, 7.[N II]/Ha-[O II]/Hb,  8.[S II]/Ha-[O I]/Ha,   9.[O I]/Ha-[O II]/Hb,  10.[S II]/Ha-[O II]/Hb
# The default value of the emission lines is 0.01. This means that if one or more emission lines are not available 
# they can be skipped (of course in this case the diagnsotics that use these lines cannot be calculated). 
# There is no default diagnostic so it should be always defined.
########################################################################################################################
factors_2d = []
with open('factors_2d.txt', 'r') as f:
        for line in f.readlines()[1:]:
            factors_2d.append(line.split())
a30 = (np.array(factors_2d[0][1:])).astype(float)
a21 = (np.array(factors_2d[1][1:])).astype(float)
a20 = (np.array(factors_2d[2][1:])).astype(float)
a12 = (np.array(factors_2d[3][1:])).astype(float)
a11 = (np.array(factors_2d[4][1:])).astype(float)
a10 = (np.array(factors_2d[5][1:])).astype(float)
a03 = (np.array(factors_2d[6][1:])).astype(float)
a02 = (np.array(factors_2d[7][1:])).astype(float)
a01 = (np.array(factors_2d[8][1:])).astype(float)
a00 = (np.array(factors_2d[9][1:])).astype(float)


PARSER = argparse.ArgumentParser()
PARSER.add_argument('-ha', '--Ha', type=float, default=0.01)
PARSER.add_argument('-sii', '--SII', type=float, default=0.01)
PARSER.add_argument('-nii', '--NII', type=float, default=0.01)
PARSER.add_argument('-oi', '--OI', type=float, default=0.01)
PARSER.add_argument('-oii', '--OII', type=float, default=0.01)
PARSER.add_argument('-oiii', '--OIII', type=float, default=0.01)
PARSER.add_argument('-hb', '--Hb', type=float, default=0.01)
PARSER.add_argument('-diag', '--diagnostics', type=str, default=None) 


    
diagn = ['SII-NII', 'NII-OIII', 'SII-OIII', 'OI-OIII', 'NII-OI', 'OII-OIII', 'NII-OII', 'SII-OI', 'OI-OII', 'SII-OII']

     
def f_2d(Ha, SII, NII, OI, OII, OIII, Hb, diagnostic):
	x = [np.log10(SII/Ha), np.log10(NII/Ha), np.log10(SII/Ha), np.log10(OI/Ha), np.log10(NII/Ha),np.log10(OII/Hb), np.log10(NII/Ha), 
     np.log10(SII/Ha), np.log10(OI/Ha), np.log10(SII/Ha)]

	y = [np.log10(NII/Ha), np.log10(OIII/Hb), np.log10(OIII/Hb), np.log10(OIII/Hb), np.log10(OI/Ha), np.log10(OIII/Hb), np.log10(OII/Hb),
     np.log10(OI/Ha), np.log10(OII/Hb), np.log10(OII/Hb)]
     
	ind = np.where(np.array(diagn)==diagnostic)[0][0]
	f = (a30[ind]*x[ind]**3.0 + a21[ind]*x[ind]**2.0*y[ind] + a20[ind]*x[ind]**2.0 + a12[ind]*x[ind]*y[ind]**2.0 + a11[ind]*x[ind]*y[ind] + 
                           a10[ind]*x[ind] + a03[ind]*y[ind]**3.0 + a02[ind]*y[ind]**2.0 + a01[ind]*y[ind] + a00[ind])
	if f > 0:
		res = 'yes'
	else:
		res = 'no'
			
	return diagnostic, res, f 

if __name__ == '__main__':
    args = PARSER.parse_args()
    f_2d(args.Ha, args.SII, args.NII, args.OI, args.OII, args.OIII, args.Hb, args.diagnostics) 


print(f_2d(args.Ha, args.SII, args.NII, args.OI, args.OII, args.OIII, args.Hb, args.diagnostics))





		
