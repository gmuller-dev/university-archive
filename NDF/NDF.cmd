@echo off
echo ---------------------------------------------------
echo 	Compile
echo ---------------------------------------------------
echo #INCLUDE NDF.h> NDF.txt
echo #INCLUDE ossbo.h>> NDF.txt
dir *.phs /b /o:n >> NDF.txt
P:\TOOLS\sqllib\sqllib.exe -C -lNDF.phs -nNDF NDF.txt
echo ---------------------------------------------------
echo 	Copy
echo ---------------------------------------------------
copy NDF.phs W:\osl\OSSBO_GUILLAUME
echo ---------------------------------------------------
echo 	Delete
echo ---------------------------------------------------
del NDF.phs
del NDF.txt
echo ---------------------------------------------------
