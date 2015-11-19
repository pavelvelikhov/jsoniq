for $x in collection()
where $x.name = "John"
return
  {"new_object":
     {$x.name : $x }
  }
