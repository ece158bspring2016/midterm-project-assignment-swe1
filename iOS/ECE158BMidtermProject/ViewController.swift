//
//  ViewController.swift
//  ECE158BMidtermProject
//
//  Created by Max X on 4/23/16.
//  Copyright © 2016 Max Xing. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var x:Int = 1

    @IBOutlet weak var tempDisplay: UILabel!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // Do any additional setup after loading the view, typically from a nib.
        
        
        
        
        NSTimer.scheduledTimerWithTimeInterval(1.0, target: self, selector: ("updateLabel"), userInfo: nil, repeats: true);
    
    
    }
    
    
    func updateLabel(){
        
        let myRootRef = Firebase(url:"https://ece158bmidterm.firebaseio.com/Temperature")


        // Read data and react to changes
        myRootRef.observeEventType(.Value, withBlock: {
            snapshot in
            print("\(snapshot.key) -> \(snapshot.value)")
            print("integervalue is ", snapshot.value.integerValue)

            self.x = snapshot.value.integerValue
            self.tempDisplay.text = String(snapshot.value) + " Celsius"

        })
        
        
        var color = UIColor(red: CGFloat(x), green: 0, blue: 0, alpha: 1)
        
        UIView.animateWithDuration(5, animations: {
            self.view.backgroundColor = color
            })
        
        
        
   /*
        let gradient: CAGradientLayer = CAGradientLayer()

        if(self.x < 10){
            gradient.colors = [UIColor.blueColor().CGColor, UIColor.whiteColor().CGColor]
        }
        else {
            gradient.colors = [UIColor.redColor().CGColor, UIColor.whiteColor().CGColor]
            
        }
    
        
        gradient.locations = [0.0 , 1.0]
        gradient.startPoint = CGPoint(x: 0.0, y: 0.0)
        gradient.endPoint = CGPoint(x: 1.0, y: 1.0)
        gradient.frame = CGRect(x: 0.0, y: 0.0, width: self.view.frame.size.width, height: self.view.frame.size.height)
        
        self.view.layer.insertSublayer(gradient, atIndex: 0)
        
        
        */
    }
    
    
    

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    


    
    
}

