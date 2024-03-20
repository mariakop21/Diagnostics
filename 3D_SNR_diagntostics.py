import numpy as np
import argparse

############################################### 2-dimensional diagnostics ##############################################
# This code checks if a source is a candidate Supernova Remnnant (SNR) or not, 
# based on 2D diagnostics developed by Kopsacheili M. et al, 2020, MNRAS, 491, 889.
# One should run: 
# python 3D_SNR_diagntostics.py -ha [x1] -sii [x2] -nii [x3]  -oi [x4] -oii [x5] -oiii [x6] -hb [x7] -diag [diagntostic]
# where [x1], [x2], ..... [x7] is the observed flux/luminosity of a source  of:
# Hα(6563), [S II](6717,6731), [N II](6583), [O I](6300), [O II](3729,3731), [O III](5007), Hβ(4681) respectively.
# The parameter 'diag' refers to the diagnostics and it should be one of the following:
# 1.'NII-SII-OIII', 2.'NII-SII-OI', 3.'NII-SII-OII',  4.'NII-OII-OIII', 5.'NII-OI-OII', 
# 6.'NII-OI-OIII',  7.'SII-OI-OII', 8.'SII-OII-OIII', 9.'SII-OI-OIII', 10.'OI-OII-OIII'
# Those are the diagntostics that combine the emission line ratios: 
# 1.[N II]/Ha-[S II]/Ha-[O III]/Hb,  2.[N II]/Ha-[S II]/Ha-[O I]/Ha, 3.[N II]/Ha-[S II]/Ha-[O II]/Hb,  4.[N II]/Ha-[O II]/Hb-[O III]/Hb, 5.[N II]/Ha-[O I]/Ha-[O II]/Hb
# 6.[N II]/Ha-[O I]/Ha-[O III]/Hb,   7.[S II]/Ha-[O I]/Ha-[O II]/Hb, 8.[S II]/Ha-[O II]/Hb-[O III]/Hb, 9.[S II]/Ha-[O I]/Ha-[O III]/Hb, 10.[O I]/Ha-[O II]/Hb-[O III]/Hb
# The default value of the emission lines is 0.01. This means that if one or more emission lines are not available 
# they can be skipped (of course in this case the diagnsotics that use these lines cannot be calculated). 
# There is no default diagnostic so it should be always defined.
########################################################################################################################
factors_2d = []
with open('factors_3d.txt', 'r') as f:
        for line in f.readlines()[1:]:
            factors_2d.append(line.split())
a300 = (np.array(factors_2d[0][1:])).astype(float)
a201 = (np.array(factors_2d[1][1:])).astype(float)
a210 = (np.array(factors_2d[2][1:])).astype(float)
a200 = (np.array(factors_2d[3][1:])).astype(float)
a102 = (np.array(factors_2d[4][1:])).astype(float)
a111 = (np.array(factors_2d[5][1:])).astype(float)
a101 = (np.array(factors_2d[6][1:])).astype(float)
a120 = (np.array(factors_2d[7][1:])).astype(float)
a110 = (np.array(factors_2d[8][1:])).astype(float)
a100 = (np.array(factors_2d[9][1:])).astype(float)
a003 = (np.array(factors_2d[10][1:])).astype(float)
a012 = (np.array(factors_2d[11][1:])).astype(float)
a002 = (np.array(factors_2d[12][1:])).astype(float)
a021 = (np.array(factors_2d[13][1:])).astype(float)
a011 = (np.array(factors_2d[14][1:])).astype(float)
a001 = (np.array(factors_2d[15][1:])).astype(float)
a030 = (np.array(factors_2d[16][1:])).astype(float)
a020 = (np.array(factors_2d[17][1:])).astype(float)
a010 = (np.array(factors_2d[18][1:])).astype(float)
a000 = (np.array(factors_2d[19][1:])).astype(float)

print(a300, a201, a210, a200, a102, a111, a101, a120, a110, a100, a003, a012, a002, a021, a011, a001, a030, a020, a010, a000)

PARSER = argparse.ArgumentParser()
PARSER.add_argument('-ha', '--Ha', type=float, default=0.01)
PARSER.add_argument('-sii', '--SII', type=float, default=0.01)
PARSER.add_argument('-nii', '--NII', type=float, default=0.01)
PARSER.add_argument('-oi', '--OI', type=float, default=0.01)
PARSER.add_argument('-oii', '--OII', type=float, default=0.01)
PARSER.add_argument('-oiii', '--OIII', type=float, default=0.01)
PARSER.add_argument('-hb', '--Hb', type=float, default=0.01)
PARSER.add_argument('-diag', '--diagnostics', type=str, default=None) 


    
diagn = ['NII-SII-OIII', 'NII-SII-OI', 'NII-SII-OII', 'NII-OII-OIII', 'NII-OI-OII', 'NII-OI-OIII', 'SII-OI-OII', 'SII-OII-OIII', 
         'SII-OI-OIII', 'OI-OII-OIII']

     
def f_2d(Ha, SII, NII, OI, OII, OIII, Hb, diagnostic):
	x = [np.log10(NII/Ha), np.log10(NII/Ha), np.log10(NII/Ha), np.log10(NII/Ha), np.log10(NII/Ha),np.log10(NII/Ha), np.log10(SII/Ha), 
         np.log10(SII/Ha), np.log10(SII/Ha), np.log10(OI/Ha)]

	y = [np.log10(SII/Ha), np.log10(SII/Ha), np.log10(SII/Ha), np.log10(OII/Hb), np.log10(OI/Ha), np.log10(OI/Ha), np.log10(OI/Ha),
         np.log10(OII/Hb), np.log10(OI/Ha),  np.log10(OII/Hb)]
     
	z = [np.log10(OIII/Hb), np.log10(OI/Ha), np.log10(OII/Hb), np.log10(OIII/Hb), np.log10(OII/Hb), np.log10(OIII/Hb), np.log10(OII/Hb),
         np.log10(OIII/Hb), np.log10(OIII/Hb), np.log10(OIII/Hb)] 
     
	ind = np.where(np.array(diagn)==diagnostic)[0][0]
	f = (a300[ind]*x[ind]**3 + a201[ind]*x[ind]**2*z[ind] + a210[ind]*x[ind]**2*y[ind] + a200[ind]*x[ind]**2 + a102[ind]*x[ind]*z[ind]**2 + 
	     a111[ind]*x[ind]*y[ind]*z[ind] + a101[ind]*x[ind]*z[ind] + a120[ind]*x[ind]*y[ind]**2 + a110[ind]*x[ind]*y[ind] + a100[ind]*x[ind] 
	     + a003[ind]*z[ind]**3 + a012[ind]*y[ind]*z[ind]**2 + a002[ind]*z[ind]**2 + a021[ind]*y[ind]**2*z[ind] + a011[ind]*y[ind]*z[ind] + 
	     a001[ind]*z[ind] + a030[ind]*y[ind]**3 + a020[ind]*x[ind]*y[ind]**2 + a010[ind]*y[ind] + a000[ind])
	if f > 0:
		res = 'yes'
	else:
		res = 'no'
			
	return diagnostic, res, f 

if __name__ == '__main__':
    args = PARSER.parse_args()
    f_2d(args.Ha, args.SII, args.NII, args.OI, args.OII, args.OIII, args.Hb, args.diagnostics) 


print(f_2d(args.Ha, args.SII, args.NII, args.OI, args.OII, args.OIII, args.Hb, args.diagnostics))
