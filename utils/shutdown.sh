echo "Calling Shutdown..."
sleep 1
response=$(curl --silent 'http://localhost:5000/quit')
if [ "$response" == "Appliation shutting down..." ];
then
  echo
  echo "Application shutdown successful"
  echo
else
 echo
 echo "Shutdown Error: No Flask Application Running"
 echo
fi
