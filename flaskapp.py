<?xml version="1.0" encoding="utf-8"?>
<!-- Created by Leo: http://leoeditor.com/leo_toc.html -->
<leo_file xmlns:leo="http://leoeditor.com/namespaces/leo-python-editor/1.1" >
<leo_header file_format="2"/>
<vnodes>
<v t="ekr.20180405105738.1"><vh>Learning to be a Leo developer</vh>
<v t="ekr.20160315141648.1"><vh>Code academy</vh>
<v t="ekr.20160315141648.3"><vh>CA: uA's</vh></v>
<v t="ekr.20160315141648.4"><vh>CA: icons</vh></v>
<v t="ekr.20160315141648.5"><vh>CA: using git</vh></v>
<v t="ekr.20160315141648.6"><vh>CA: finding nodes with c.cloneFindByPredicate</vh></v>
</v>
<v t="ekr.20180405093138.1"><vh>Leo University</vh></v>
</v>
</vnodes>
<tnodes>
<t tx="ekr.20160315141648.1">@language rest
@wrap

Leo's Code Academy posts discuss how to do useful things in Leo. The following are distilled from online discussions about Leo's scripting.</t>
<t tx="ekr.20160315141648.3">uA's (user Attributes) associate arbitrary data with any vnode. uA's are dictionaries of dictionaries--an **outer dictionary** and zero or more **inner dictionaries**. The outer dictionary associates plugin names (or Leo's core) with inner dictionaries. The inner dictionaries carry the actual data.

The v.u or p.v properties get and set uA's. You can think of p.u as a synonym for p.v.unknownAttributes on both sides of an assignment. For example::

    plugin_name = 'test_plugin'
    d = p.u.get(plugin_name,{})
    d ['n'] = 8
    p.u [plugin_name] = d

p.u is the outer dictionary. p.u.get.(plugin_name, {}) is the inner dictionary. The last line is all that is needed to update the outer dictionary!

It is easy to search for particular uA's. The following script prints all the keys in the outer-level uA dictionaries:

    for p in c.all_unique_positions():
        if p.u:
            print(p.h, sorted(p.u.keys()))

This is a typical usage of Leo's generators.  Generators visit each position (or node) quickly. Even if you aren't going to program much, you should be aware of how easy it is to get and set the data in each node. In fact, now would be a great time to read Leo's Scripting Tutorial again :-) This will allow you to "dream bigger" with Leo.

The following script creates a list of all positions having an icon, that is, an outer uA dict with a 'icon' key.

    aList = [p.copy() for p in c.all_unique_positions() if 'icon' in p.u]
    print('\n'.join([p.h for p in aList]))

*Important*: If you don't understand these lines, please study Python's list comprehensions.  They are incredibly useful. '\n'.join(aList) is a great idiom to know.  str.join is one of python's most useful string methods. It converts between lists and strings.
</t>
<t tx="ekr.20160315141648.4">@language rest

This script inserts three icons in the current outline node. Running the script again will insert three more::

@language python

    table = (
        'edittrash.png',
        'connect_no.png',
        'error.png',
    )
    for icon in table:
        fn = g.os_path_finalize_join(g.app.loadDir,
            '..', 'Icons', 'Tango', '16x16', 'status', icon)
        if g.os_path_exists(fn):
            c.editCommands.insertIconFromFile(path=fn)
        
@language rest
        
This deletes all icons of the node at position p::

    c.editCommands.deleteNodeIcons(p=p)
</t>
<t tx="ekr.20160315141648.5">Using Leo’s latest sources from GitHub is highly recommended. Once git is installed, the following gets the latest Leo sources::

    git clone https://github.com/leo-editor/leo-editor.git

Thereafter, you can update Leo's sources with::

    git pull

Git is great in tracking history and reverting unwanted changes. And it has many other benefits.

Using git is very similar to using bzr or hg or any other SCCS.  To change Leo, you add files, you commit files, and you push files.  That's about it.
</t>
<t tx="ekr.20160315141648.6">@language rest

c.cloneFindByPredicate is a powerful new addition to Leo.  Here is its docstring:

    Traverse the tree given using the generator, cloning all positions for
    which predicate(p) is True. Undoably move all clones to a new node, created
    as the last top-level node. Returns the newly-created node. Arguments:

    generator,      The generator used to traverse the tree.
    predicate,      A function of one argument p returning true if p should be included.
    failMsg=None,   Message given if nothing found. Default is no message.
    flatten=False,  True: Move all node to be parents of the root node.
    iconPath=None,  Full path to icon to attach to all matches.
    redraw=True,    True: redraw the screen.
    undo_type=None, The undo/redo name shown in the Edit:Undo menu.
                    The default is 'clone-find-predicate'
                    
For example, clone-find-all-marked command is essentially:
    
@language python

    @cmd('clone-find-all-marked')
    def cloneFindMarked(self, flatten):
        
        def isMarked(p):
            return p.isMarked()
            
        self.cloneFindByPredicate(
            generator = self.all_unique_positions,
            predicate = isMarked,
            failMsg = 'nothing found',
            flatten = flatten,
            undoType = 'clone-find-marked',
        )
        
@language rest

The predicate could filter on an attribute or *combination* of attributes. For example, the predicate could return p has attributes A and B but *not* attribute C. This instantly gives Leo full database query capabilities. If we then hoist the resulting node we see *all and only* those nodes satisfying the query.

These following position methods make it easy to skip @ignore trees or @&lt;file&gt; trees containing @all::
        
    p.is_at_all()          True if p is an @&lt;file&gt; node containing an @all directive.
    p.in_at_all()          True if p is in an @&lt;file&gt; tree whose root contains @all.
    p.is_at_ignore()       True if p is an @ignore node
    p.in_at_ignore_tree()  True if p is in an @ignore tree.

For example, here is how to gather only those marked nodes that lie outside any @ignore tree::

@language python

    def isMarked(p):
        return p.isMarked() and not p.in_at_ignore_tree()
      
    c.cloneFindByPredicate(
        generator = self.all_unique_positions,
        predicate = isMarked,
        flatten = flatten,
        undoType = 'gather-marked',
    )
</t>
<t tx="ekr.20180405093138.1">Leo University is a project devoted to help people become Leo developers.

Here is the main page.  It contains links to individual lessons.
https://github.com/leo-editor/leo-editor/issues/816
</t>
<t tx="ekr.20180405105738.1"></t>
</tnodes>
</leo_file>
