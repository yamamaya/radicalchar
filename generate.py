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
    
    print( "Generating a source code for JavaScript ... ", end="" )
    with open( "radicalchar.js", "w" ) as dest:
        print( """\
class RadicalChar {
    static convlist = {""", file=dest )
        for t in list:
            print( "        '{0}': '{1}',  // {2} : {3}".format( t[0], t[1], format( ord( t[0] ), "x" ), format( ord( t[1] ), "x" ) ), file=dest )
        print( """\
    };

    static Normalize( str ) {
        Object.keys( RadicalChar.convlist ).map( a => {
            if ( str.indexOf( a ) != -1 ) {
                str = str.replaceAll( a, RadicalChar.convlist[a] );
            }
            return str;
        } );
        return str;
    }
}""", file=dest )
    print( "done" )

    print( "Generating a source code for Python ... ", end="" )
    with open( "radicalchar.py", "w" ) as dest:
        print( "convlist = {", file=dest )
        for t in list:
            print( "    '{0}': '{1}',  # {2} : {3}".format( t[0], t[1], format( ord( t[0] ), "x" ), format( ord( t[1] ), "x" ) ), file=dest )
        print( """\
}

def normalize( str ):
    for a, b in convlist.items():
        if a in str:
            str = str.replace( a, b )
    return str""", file=dest )
    print( "done" )

    print( "Generating a source code for C# ... ", end="" )
    with open( "radicalchar.cs", "w" ) as dest:
        print( """\
using System.Collections.Generic;

class RadicalChar {
    public static readonly Dictionary<char,char> convlist = new Dictionary<char,char> {""", file=dest );
        for t in list:
            print( "        {{ '{0}', '{1}' }},  // {2} : {3}".format( t[0], t[1], format( ord( t[0] ), "x" ), format( ord( t[1] ), "x" ) ), file=dest )
        print( """\
    };

    static public string Normalize( string str ) {
        foreach ( KeyValuePair<char, char> t in convlist ) {
            if ( str.IndexOf( t.Key ) != -1 ) {
                str = str.Replace( t.Key, t.Value );
            }
        }
        return str;
    }
}""", file=dest );
    print( "done" )
    
    print( "All files generated successfully." )

except:
    print( "ERROR" )
