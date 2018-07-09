* Setting up

   see ```/nfs/cnhlab001/cnh/conda-setups/pangeo-and-jupyterlab/setup.sh ```
   
* MUR SST files
   
   ```/nfs/cnhlab003/cnh/mur-sst/```
   
* Get going with jupyter
  
  - This involves (i) reserving a compute node using ```srun```, (2) using a program called ```screen``` to save
    login sessions even when you are logged out.
  - Here are some commands
     ```
     # Register your key (only need to do once when boot laptop)
     ssh-add /Users/chrishill/.ssh/id_rsa
     
     # Log in to cluster, start Jupyter in a screen session
     ssh -l cnh eofe7.mit.edu
     # cat ~/bin/sjlab.sh
     screen
      ^a^d
     screen -list
     screen -r -d
      ~/bin/sjlab.sh
      ^a^d
      
      # Log in to cluster, forward port 8888 on "localhost" (your laptop) to port
      # 8888 on the cluster compute node (e.g. node757 ) - an ssh tunnel! 
      ssh -L 8888:node757.ib.cluster:8888  -l cnh eofe7.mit.edu  
      
      
      
      
     ```

* Using Git notes

  Some words from Allison and some more
