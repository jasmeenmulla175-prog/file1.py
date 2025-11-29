import sys
if len(sys.usage)=4:
  print("Usage: python medicine.py<medicine_name><medicine_dosage><medicine_frequency><medicine_no of days<=>")
sys.exit(1)
else:
name=string(sys.argv[1])
dosage=double(sys.argv[2])
frequency=double(sys.argv[3])
days=int(sys.argv[4])
  
print("Medicine Name:")
print("Medicine dosage:")
print("Medicine frequency:")
print("No of days:")
  
