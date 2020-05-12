//
//  ViewController.swift
//  Internet Device
//
//  Created by Aashish Saini on 4/16/20.
//  Copyright © 2020 Aashish Saini. All rights reserved.
//

import UIKit
import WebKit
class ViewController: UIViewController, WKNavigationDelegate {

    @IBOutlet var webView: WKWebView!
    
    @IBOutlet var activityind: UIActivityIndicatorView!
    override func viewDidLoad() {
        super.viewDidLoad()
        let myURL = URL(string:"https://www.parkcircletech.com/")
        let myRequest = URLRequest(url: myURL!)
        webView.load(myRequest)
        webView.addSubview(self.activityind)
        self.webView.navigationDelegate = self
        activityind.startAnimating()
        activityind.hidesWhenStopped = true
        // Do any additional setup after loading the view.
    }
    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
                     activityind.stopAnimating()
                 }
       func webView(_ webView: WKWebView, didFail navigation: WKNavigation!, withError error: Error) {

                     activityind.stopAnimating()
                 }


}

