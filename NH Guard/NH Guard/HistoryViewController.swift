//
//  HistoryViewController.swift
//  NH Guard
//
//  Created by Aashish Saini on 4/5/20.
//  Copyright © 2020 Aashish Saini. All rights reserved.
//

//
//  unitsViewController.swift
//  NH Guard
//
//  Created by Aashish Saini on 4/4/20.
//  Copyright © 2020 Aashish Saini. All rights reserved.
//


import UIKit
import WebKit
class HistoryViewController: UIViewController,WKNavigationDelegate{
    
    @IBOutlet var historybackbutton: UIImageView!
    
    @IBOutlet var loading: UILabel!
    @IBOutlet var myWebView: WKWebView!
    
    @IBOutlet var activityind: UIActivityIndicatorView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        let myURL = URL(string:"https://nh.ng.mil/History/")
        let myRequest = URLRequest(url: myURL!)
        myWebView.load(myRequest)
        myWebView.addSubview(self.activityind)
        self.myWebView.navigationDelegate = self
        activityind.startAnimating()
        activityind.hidesWhenStopped = true
        
        let tapGesture4 = UITapGestureRecognizer(target: self, action: #selector(imageTapped4))

                    // add it to the image view;
                    historybackbutton.addGestureRecognizer(tapGesture4)
                    // make sure imageView can be interacted with by user
                historybackbutton.isUserInteractionEnabled = true
               
                }
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        loading.isHidden = true

               activityind.stopAnimating()
           }
    func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {
        loading.isHidden = true

               activityind.stopAnimating()
           }
            
        @objc func imageTapped4(gesture: UIGestureRecognizer) {
            // if the tapped view is a UIImageView then set it to imageview
        if (gesture.view as? UIImageView) != nil {
                self.performSegue(withIdentifier: "HomeScreenSague", sender: self)
                //Here you can initiate your new ViewController

                }
            }


            // Do any additional setup after loading the view.
        }




