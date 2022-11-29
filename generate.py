try:
    print( "Reading source file ... ", end="" )
    src = open( "raw list.txt" )
    lines = src.read().splitlines()
    src.close()
    print( "done" )
    
    list = []
    for line in lines:
        t = line.split( "\t" )
        list.append( t )
        print( t[0], format( ord( t[0] ), "x" ), t[1], format( ord( t[1] ), "x" ), sep="\t" )
    print( "" )
    
    print( "Generating a list file for JavaScript ... ", end="" )
    with open( "radicalchar.js", "w" ) as dest:
        print( "var convlist = {", file=dest )
        for t in list:
            print( "    '{0}': '{1}',  // {2} : {3}".format( t[0], t[1], format( ord( t[0] ), "x" ), format( ord( t[1] ), "x" ) ), file=dest )
        print( "};", file=dest )
    print( "done" )
    
    print( "Generating a list file for Python ... ", end="" )
    with open( "radicalchar.py", "w" ) as dest:
        print( "convlist = {", file=dest )
        for t in list:
            print( "    '{0}': '{1}',  # {2} : {3}".format( t[0], t[1], format( ord( t[0] ), "x" ), format( ord( t[1] ), "x" ) ), file=dest )
        print( "}", file=dest )
    print( "done" )
    
    print( "Generating a list file for C# ... ", end="" )
    with open( "radicalchar.cs", "w" ) as dest:
        print( "using System.Collections.Generic;", file=dest );
        print( "", file=dest );
        print( "class RadicalChar {" , file=dest )
        print( "    public static readonly Dictionary<char,char> convlist = new Dictionary<char,char> {", file=dest )
        for t in list:
            print( "        {{ '{0}', '{1}' }},  // {2} : {3}".format( t[0], t[1], format( ord( t[0] ), "x" ), format( ord( t[1] ), "x" ) ), file=dest )
        print( "    };", file=dest )
        print( "}", file=dest )
    print( "done" )
    
    print( "All files generated successfully." )

except:
    print( "ERROR" )
