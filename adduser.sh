#!/bin/bash

execute(){
    #Greet users
    echo "Welcome to the User Creation Application"
    echo "This application will help you create a user" 
 
    ans="yes"

    while [ $ans == "yes" ]
    do 

    #create user for the first time by calling the createUser function
    createUser
    
    #ask user if they want to add another user
    #check that it is a valid answer
    promptUser


    #if answer is yes the if statement will be skipped and loop again
    #if answer is no the answer will be no and exit out the loop
         
        if [ $ans == "no" ]
        then
            echo "Thank you for using the application"
        fi

    done

}

promptUser(){

    #if user does not yes or no, they are prompted to answer a valid answer
    validAns=false

    
    while [ "$validAns" = false ]
    do
    echo "Would you like to add another user? Please answer yes or no:"
    read ans
 
        echo
        if [ $ans == "yes" ] || [ $ans == "no" ]
        then
            validAns=true
        else
            echo "Please enter a vaid answer: yes or no"
        fi
    done

        } 

createUser(){

        echo "What is the user's name?"
        read name
        echo "What is the group's name?"
        read group
        echo "Creating user $name"

        #create user and group using sudo because they can only be created in root
        sudo useradd $name
        echo "Creating group $group"
        sudo groupadd $group
        echo "Adding user $name  to the user group $group"
        sudo usermod -aG $group  $name
        id $name
    }


execute





