class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


class Nail:
    def __init__(self,width,height) -> None:
        self.widths = width
        self.heights = height
    

    def nailDescriptionOnSize(self):

        c = color()
        width = float()
        height = float()
        if len(self.widths)==0:
            return "no nail", 0 , 0
        else:
            for i in range(len(self.widths)):
                width += self.widths[i]
                height += self.heights[i]

        widPrcnt = round((width / (width + height)) * 100)
        hghtPrcnt = round((height / (width + height)) * 100)
        
        if width > height * 1.5:
            nailSize = f"Long and wide"
            print(f"{c.BOLD}{c.GREEN}You have a long, wide nail{c.END}\n")
            print("These are the recommended nail polish for you:")
            print(f"You can pick among {c.UNDERLINE}nude{c.END}, {c.UNDERLINE}bold{c.END}, {c.UNDERLINE}sheer{c.END}, or {c.UNDERLINE}opaque{c.END}")
            print(f"{c.UNDERLINE}Oval{c.END} and {c.UNDERLINE}almond{c.END} shape will look good on your nail")
            print("Avoid long pointed or square nails shape")
    
        elif width > height:
            nailSize = f"short and wide"
            print(f"{c.BOLD}{c.PURPLE}You have a short and wide nail{c.END}\n")
            print("I can recommend these nail polish for you:")
            print(f"{c.UNDERLINE}Sheer nudes{c.END} or {c.UNDERLINE}slippery metalics{c.END} like Rose Gold")
            print(f"You can also cut your nails to {c.UNDERLINE}round-shape{c.END} to make your nails slimmer and longer")
            print("You should avoid square and pointed nails so it will not look wide. Inky black and blues will make your nail look harsh")
        
        elif height > width * 1.5:
            nailSize = f"Long and slim"
            print(f"{c.BOLD}{c.YELLOW}You have a long, slim nail{c.END}\n")
            print("These nail polish will look good on you:")
            print(f"{c.UNDERLINE}Red{c.END}, {c.UNDERLINE}burgundy{c.END}, {c.UNDERLINE}pink{c.END}, and {c.UNDERLINE}nudes{c.END}")
            print(f"I can recommend {c.UNDERLINE}square nails {c.END} on your looks")
            print("Do not use risky blues or purple colored polish as they will look cartoonish")
    
        
        elif height > width:
            nailSize = f"short and slim"
            print(f"{c.BOLD}{c.RED}You have a short, slim nail{c.END}\n")
            print("The recommended nail polish for you will be:")
            print(f"{c.UNDERLINE}Sexy red{c.END} and {c.UNDERLINE}creamy pastels {c.END} like periwinkle blue")
            print(f"{c.UNDERLINE}Squoval{c.END} and {c.UNDERLINE}round nail{c.END} shape will look good on your nail")
            print("Avoid black nail polish since it will make your nail more slimmer")

        return nailSize, widPrcnt, hghtPrcnt
    

