import numpy as np
import matplotlib.pyplot as plt
ch2='y'
while(ch2=='y'):
        ch=raw_input("Is phase angle constant enter 'p' else enter 'n'? ")
        if (ch=='p'):
                ch4=raw_input("Is frequency constant enter 'f' else enter 'n'? ")
                if(ch4=='f'):
                        ch3=raw_input("Is amplitude constant enter 'a' else enter 'n'? ")
                        if (ch3=='a'):
                                #It has constant amplitude,frequency and phase
                                #Defining the equation of SHM 
                                print 'Simple Harmonic Motion(SHM) equations:'
                                print 'Displacement: a*cos(wt+p)\nVelocity: -w*a*sin(wt+p)\nAcceleration: -w^2*a*sin(wt+p)\n\twhere a=amplitude\n\tw=angular velocity=2*pi*frequency\n\tp=phase angle'
                                #Taking inputs
                                p=input('Enter the constant phase angle of shm:')
                                a=input('Enter the constant amplitude of shm:')
                                f=input( 'Enter the constant frequency of shm:')
                                t=1/f
                                x=np.arange(0,2*np.pi*f*t,0.1)
                                d=a*np.cos(x+p)
                                v=(-1)*x*a*np.sin(x+p)
                                acc=-(x*x)*a*np.cos(x+p)
                                plt.subplot(3,2,1)
                                plt.plot(x,d)
                                plt.plot([7,0],[0,0],color='black')
                                plt.grid(True)
                                plt.title('Displacement graph')
                                plt.subplot(3,2,2)
                                plt.plot(x,v)
                                plt.plot([7,0],[0,0],color='black')
                                plt.grid(True)
                                plt.title('Velocity graph')
                                plt.subplot(3,1,3)
                                plt.plot(x,acc)
                                plt.plot([7,0],[0,0],color='black')
                                plt.grid(True)
                                plt.title('Acceleration graph')
                                #for showing the graph
                                plt.show()
                        else:
                                #It has constant frequency and phase with different amplitude
                                #Declaring variable as empty array
                                a=[None]*1000
                                #Defining the equation of SHM 
                                print 'Simple Harmonic Motion(SHM) equations:'
                                print 'Displacement: a*cos(wt+p)\nVelocity: -w*a*sin(wt+p)\nAcceleration: -w^2*a*sin(wt+p)\n\twhere a=amplitude\n\tw=angular velocity=2*pi*frequency\n\tp=phase angle'
                                #Taking inputs
                                j = input('Enter the number of elements:')
                                p=input('Enter the constant phase angle of shm:')
                                f=input ('Enter the constant frequency of shm:')
                                print 'Enter the amplitude:'
                                for i in range (j):
                                        a[i]=input(' ')
                                t=1/f
                                x=np.arange(0,2*np.pi*f*t,0.1)
                                x1=0
                                #Calculating all quantites and plotting on graph
                                for i in range(j):
                                        d=a[i]*np.cos(x+p)
                                        v=(-1)*x*a[i]*np.sin(x+p)
                                        acc=-(x*x)*a[i]*np.cos(x+p)
                                        x1=x1+a[i]
                                        plt.subplot(2,2,1)
                                        plt.plot(x,d)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Displacement graph')
                                        plt.subplot(2,2,2)
                                        plt.plot(x,v)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.title('Velocity graph')
                                        plt.grid(True)
                                        plt.subplot(2,2,3)
                                        plt.plot(x,acc)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Acceleration graph')
                                x1=x1*np.cos(x+p)
                                plt.subplot(2,2,4)
                                plt.plot(x,x1)  
                                plt.plot([7,0],[0,0],color='black')
                                plt.grid(True)
                                plt.title('Superimposed of all shm')
                                #for showing the graph 
                                plt.show()
                if (ch4=='n'):
                        ch5=raw_input("Is amplitude constant enter 'a' else enter 'n'? ")
                        if(ch5=='a'):
                                #It has constant amplitude and phase with different freqeuncy
                                #Declaring variable as empty array
                                f=[None]*1000
                                t=[None]*1000
                                #Defining the equation of SHM 
                                print 'Simple Harmonic Motion(SHM) equations:'
                                print 'Displacement: a*cos(wt+p)\nVelocity: -w*a*sin(wt+p)\nAcceleration: -w^2*a*sin(wt+p)\n\twhere a=amplitude\n\tw=angular velocity=2*pi*frequency\n\tp=phase angle'
                                #Taking inputs
                                j = input('Enter the number of elements:')
                                p=input('Enter the constant phase angle of shm:')
                                c=0
                                a=input ('Enter the constant amplitude of shm:')
                                print 'Enter the frequency:'
                                for i in range (j):
                                        f[i]=input(' ')
                                x1=0
                                #Calculating all quantites and plotting on graph
                                for i in range(j):
                                        t[i]=1/f[i]
                                        x=np.arange(0,2*np.pi*f[i]*t[i],0.1)
                                        d=a*np.cos(x+p)
                                        v=(-1)*x*a*np.sin(x+p)
                                        acc=-(x*x)*a*np.cos(x+p)
                                        x1=x1+np.cos(x+c*p)
                                        c=c+1
                                        plt.subplot(2,2,1)
                                        plt.plot(x,d)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Displacement graph')
                                        plt.subplot(2,2,2)
                                        plt.plot(x,v)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Velocity graph')
                                        plt.subplot(2,2,3)
                                        plt.plot(x,acc)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Acceleration graph')
                                x1=x1*a
                                plt.subplot(2,2,4)
                                plt.plot(x,x1)  
                                plt.plot([7,0],[0,0],color='black')
                                plt.grid(True)
                                plt.title('Superimposed of all shm')
                                #for showing the graph 
                                plt.show()
                        else:
                                #It has constant phase angle with different apmlitude,frequency
                                #Declaring variable as empty array
                                f=[None]*1000
                                a=[None]*1000
                                t=[None]*1000
                                #Defining the equation of SHM 
                                print 'Simple Harmonic Motion(SHM) equations:'
                                print 'Displacement: a*cos(wt+p)\nVelocity: -w*a*sin(wt+p)\nAcceleration: -w^2*a*sin(wt+p)\n\twhere a=amplitude\n\tw=angular velocity=2*pi*frequency\n\tp=phase angle'
                                #Taking inputs
                                j = input('Enter the number of elements:')
                                p=input('Enter the constant phase angle of shm:')
                                print 'Enter the frequency of shm:'
                                for i in range (j):
                                        f[i]=input(' ')
                                print 'Enter the amplitude of shm:'
                                for i in range(j):
                                        a[i]=input(' ')
                                d1=0
                                #Calculating all quantities and plotting on graph
                                for i in range(j):
                                        t[i]=1/f[i]
                                        x=np.arange(0,2*np.pi*f[i]*t[i],0.1)
                                        d=a[i]*np.cos(x+p)
                                        d1=d1+d
                                        v=(-1)*x*a[i]*np.sin(x+p)
                                        acc=-(x*x)*a[i]*np.cos(x+p)
                                        plt.subplot(4,1,1)
                                        plt.plot(x,d)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Displacement graph')
                                        plt.subplot(4,1,2)
                                        plt.plot(x,v)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Velocity graph')
                                        plt.subplot(4,1,3)
                                        plt.plot(x,acc)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Acceleration graph')
                                plt.subplot(4,1,4)
                                plt.plot(x,d1)  
                                plt.plot([7,0],[0,0],color='black')
                                plt.grid(True)
                                plt.title('Superimposed of all shm')
                                #for showing the graph
                                plt.show()
        else:
                ch6=raw_input("Is frequency constant enter 'f' else enter 'n'? ")
                if(ch6=='f'):
                        ch7=raw_input("Is amplitude constant enter 'a' else enter 'n'? ")
                        if(ch7=='a'):
                                #It has constant amplitude,frequency with different phase
                                #Declaring variable as empty array
                                p=[None]*1000
                                #Defining the equation of SHM 
                                print 'Simple Harmonic Motion(SHM) equations:'
                                print 'Displacement: a*cos(wt+p)\nVelocity: -w*a*sin(wt+p)\nAcceleration: -w^2*a*sin(wt+p)\n\twhere a=amplitude\n\tw=angular velocity=2*pi*frequency\n\tp=phase angle'
                                #Taking inputs
                                j = input('Enter the number of elements:')
                                a=input('Enter the constant amplitude of shm:')
                                f=input( 'Enter the constant frequency of shm:')
                                print 'Enter the phase angles of shm:'
                                for i  in range (j):
                                        p[i]=input(' ')
                                x1=0
                                t=1/f
                                x=np.arange(0,2*np.pi*f*i,0.1)
                                #Calculating all quantites and plotting on graph
                                for i in range(j):
        
                                        d=a*np.cos(x+p[i])
                                        x1=x1+np.cos(x+p[i])
                                        v=(-1)*x*a*np.sin(x+p[i])
                                        acc=-(x*x)*a*np.cos(x+p[i])
                                        plt.subplot(4,1,1)
                                        plt.plot(x,d)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Displacement graph')
                                        plt.subplot(4,1,2)
                                        plt.plot(x,v)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Velocity graph')
                                        plt.subplot(4,1,3)
                                        plt.plot(x,acc)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Acceleration graph')
                                x1=x1*a
                                plt.subplot(4,1,4)
                                plt.plot(x,x1)
                                plt.plot([7,0],[0,0],color='black')
                                plt.grid(True)
                                plt.title('Superimposed of all shm')
                                #for showing the graph 
                                plt.show()
                        else:
                                #It has constant frequency with different amplitude and phase
                                #Declaring variable as empty array
                                p=[None]*1000
                                a=[None]*1000
                                t=[None]*1000
                                #Defining the equation of SHM 
                                print 'Simple Harmonic Motion(SHM) equations:'
                                print 'Displacement: a*cos(wt+p)\nVelocity: -w*a*sin(wt+p)\nAcceleration: -w^2*a*sin(wt+p)\n\twhere a=amplitude\n\tw=angular velocity=2*pi*frequency\n\tp=phase angle'
                                #Taking inputs
                                j = input('Enter the number of elements:')
                                f=input( 'Enter the constant frequency of shm:')
                                print 'Enter the phase angles of shm:'
                                for i  in range (j):
                                        p[i]=input(' ')
                                print 'Enter the amplitude of shm:'
                                for i in range(j):
                                        a[i]=input (' ')
                                d1=0
                                t=1/f
                                x=np.arange(0,2*np.pi*f*i,0.1)
                                #Calculating all quantites and plotting on graph
                                for i in range(j):
                                        d=a[i]*np.cos(x+p[i])
                                        d1=d1+d
                                        v=(-1)*x*a[i]*np.sin(x+p[i])
                                        acc=-(x*x)*a[i]*np.cos(x+p[i])
                                        plt.subplot(4,1,1)
                                        plt.plot(x,d)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Displacement graph')
                                        plt.subplot(4,1,2)
                                        plt.plot(x,v)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Velocity graph')
                                        plt.subplot(4,1,3)
                                        plt.plot(x,acc)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Acceleration graph')
                                plt.subplot(4,1,4)
                                plt.plot(x,d1)  
                                plt.plot([7,0],[0,0],color='black')
                                plt.grid(True)
                                plt.title('Superimposed of all shm')
                                #for showing the graph 
                                plt.show()
                if(ch6=='n'):
                        ch8=raw_input("Is amplitude constant enter 'a' else enter 'n'? ")
                        if(ch8=='a'):
                                #It has constant amplitude with different phase angle and frequency
                                #Declaring variable as empty array
                                f=[None]*1000
                                t=[None]*1000
                                p=[None]*1000
                                #Defining the equation of SHM 
                                print 'Simple Harmonic Motion(SHM) equations:'
                                print 'Displacement: a*cos(wt+p)\nVelocity: -w*a*sin(wt+p)\nAcceleration: -w^2*a*sin(wt+p)\n\twhere a=amplitude\n\tw=angular velocity=2*pi*frequency\n\tp=phase angle'
                                #Taking inputs
                                j = input('Enter the number of elements:')
                                a=input('Enter the constant amplitude of shm:')
                                print 'Enter the frequency of shm:'
                                for i in range (j):
                                        f[i]=input(' ')
                                print 'Enter the phases of shm:'
                                for i in range (j):
                                        p[i]=input(' ')
                                d1=0
                                x1=0
                                #Calculating all quantites and plotting on graph
                                for i in range(j):
                                        t[i]=1/f[i]
                                        x=np.arange(0,2*np.pi*f[i]*t[i],0.1)
                                        d=a*np.cos(x+p[i])
                                        d1=d1+d
                                        v=(-1)*x*a*np.sin(x+p[i])
                                        acc=-(x*x)*a*np.cos(x+p[i])
                                        x1=x1+np.cos(x+p[i])
                                        plt.subplot(4,1,1)
                                        plt.plot(x,d)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Displacement graph')
                                        plt.subplot(4,1,2)
                                        plt.plot(x,v)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('\nVelocity graph')
                                        plt.subplot(4,1,3)
                                        plt.plot(x,acc)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('\nAcceleration graph')
                                x1=x1*a
                                plt.subplot(4,1,4)      
                                plt.plot(x,x1)
                                plt.plot([7,0],[0,0],color='black')
                                plt.grid(True)
                                plt.title('\nSuperimposed of all shm')  
                                #for showing the graph 
                                plt.show()
                        else:
                                #It has different amplitude,frequency and phase
                                #Declaring variable as empty array
                                f=[None]*1000
                                a=[None]*1000
                                t=[None]*1000
                                p=[None]*1000
                                #Defining the equation of SHM 
                                print 'Simple Harmonic Motion(SHM) equations:'
                                print 'Displacement: a*cos(wt+p)\nVelocity: -w*a*sin(wt+p)\nAcceleration: -w^2*a*sin(wt+p)\n\twhere a=amplitude\n\tw=angular velocity=2*pi*frequency\n\tp=phase angle'                  
                                #Taking inputs
                                j = input('Enter the number of elements:')
                                print 'Enter the phase angles of shm:'
                                for i in range (j):
                                        p[i]=input(' ')
                                print 'Enter the frequency of shm:'
                                for i in range (j):
                                        f[i]=input(' ')
                                print 'Enter the amplitude of shm:'
                                for i in range(j):
                                        a[i]=input(' ')
                                d1=0
                                #Calculating all quantites and plotting on graph
                                for i in range(j):
                                        t[i]=1/f[i]
                                        x=np.arange(0,2*np.pi*f[i]*t[i],0.1)
                                        d=a[i]*np.cos(x+p[i])
                                        d1=d1+d
                                        v=(-1)*x*a[i]*np.sin(x+p[i])
                                        acc=-(x*x)*a[i]*np.cos(x+p[i])
                                        plt.subplot(4,1,1)
                                        plt.plot(x,d)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Displacement graph')
                                        plt.subplot(4,1,2)
                                        plt.plot(x,v)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Velocity graph')
                                        plt.subplot(4,1,3)
                                        plt.plot(x,acc)
                                        plt.plot([7,0],[0,0],color='black')
                                        plt.grid(True)
                                        plt.title('Acceleration graph')
                                plt.subplot(4,1,4)
                                plt.plot(x,d1)  
                                plt.plot([7,0],[0,0],color='black')
                                plt.grid(True)
                                plt.title('Superimposed of all shm')
                                #for showing the graph 
                                plt.show()
#If the input is yes then the program again start from while loop and check the conditions
        ch2=raw_input('Want to enter more? ')
