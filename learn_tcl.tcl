for {set i 0} {$i<$argc} {incr i 1} {
	puts [ lindex $argv $i]
}
#below line helps to access each element of list index starting from 0 
puts [ lindex $argv 0]
set x [ lindex $argv 0]
puts $x

#meshfile is file varaible through which sample.txt is accessed
set meshFile [open sample.txt w] 
for {set i 0} {$i<$argc} {incr i 1} {
	puts $meshFile [ lindex $argv $i]
}
close $meshFile