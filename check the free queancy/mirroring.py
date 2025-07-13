def mirrorcharacter(input,k):
    # create dictionary
      original = 'abcdefghijklmnopqrstuvwxy'
      reverse = 'zyxwvutsrqponmlkjihgfedcba'
      dictChars = dict(zip(original,reverse))
      prefix = input[0:k-1]
      sufix = input[k-1:]
      mirror = ''
      for i in range(0,len(sufix)):
            mirror= mirror+dictChars[sufix[i]]
            print(prefix+mirror)
mirrorcharacter('letter',5)