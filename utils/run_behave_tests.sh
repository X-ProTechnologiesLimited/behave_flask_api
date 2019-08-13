#!/bin/bash
echo "Starting the Automated Test Suite..."
echo "--------------------------------------------------------------------------------"
echo "Executing Only ADD GET and UPDATE Scenarios now...Skipping DELETE Scenarios"
echo "--------------------------------------------------------------------------------"
behave --tags=~@delete --no-skipped --junit ../tests
echo "--------------------------------------------------------------------------------"
echo "Executing only DELETE Scenarios now....Skipping ADD/GET/UPDATE Scenarios"
echo "--------------------------------------------------------------------------------"
behave --tags=@delete --no-skipped --junit ../tests
