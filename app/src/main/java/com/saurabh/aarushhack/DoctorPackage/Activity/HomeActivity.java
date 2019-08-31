package com.saurabh.aarushhack.DoctorPackage.Activity;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.Toolbar;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentPagerAdapter;
import androidx.viewpager.widget.ViewPager;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.widget.Toast;

import com.google.android.material.tabs.TabLayout;
import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;
import com.pusher.client.Pusher;
import com.pusher.client.PusherOptions;
import com.pusher.client.channel.Channel;
import com.pusher.client.channel.PusherEvent;
import com.pusher.client.channel.SubscriptionEventListener;
import com.saurabh.aarushhack.DoctorPackage.Activity.Fragment.NurseFragment;
import com.saurabh.aarushhack.DoctorPackage.Activity.Fragment.PatientFragment;
import com.saurabh.aarushhack.R;

import java.util.ArrayList;
import java.util.List;

public class HomeActivity extends AppCompatActivity {

    TabLayout tabLayout;
    ViewPager viewPager;
    IntentIntegrator qrScan;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        getSupportActionBar().setTitle("AarushHack - Doctor App");

        tabLayout = findViewById(R.id.tabLayoutHome);
        viewPager = findViewById(R.id.layoutPageHome);
        tabLayout.setTabGravity(TabLayout.GRAVITY_FILL);
        tabLayout.setupWithViewPager(viewPager);

        PusherOptions options = new PusherOptions();
        options.setCluster("ap2");
        Pusher pusher = new Pusher("79dd411b1ee2c4d8a64c", options);

        Channel channel = pusher.subscribe("my-channel");

        channel.bind("my-event", new SubscriptionEventListener() {
            @Override
            public void onEvent(PusherEvent event) {
                Log.v("TAG", event.getData());
            }
        });

        pusher.connect();


        setUpViewPage(viewPager);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        MenuInflater inflater = getMenuInflater();
        inflater.inflate(R.menu.home_doctor, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        int id = item.getItemId();

        switch (id) {
            case R.id.attendanceHome:
                qrScan = new IntentIntegrator(HomeActivity.this);
                qrScan.initiateScan();
                break;
            case R.id.loginMainButton:
                break;
        }

        return super.onOptionsItemSelected(item);
    }

    public class ViewPageAdapter extends FragmentPagerAdapter {
        private List<Fragment> MyFragment = new ArrayList<>();
        private List<String> MyPageTitle = new ArrayList<String>();

        public ViewPageAdapter(FragmentManager fm) {
            super(fm);
        }

        public void AddFragmentPage(Fragment Fragment, String Title) {
            MyFragment.add(Fragment);
            MyPageTitle.add(Title);
        }

        @Nullable
        @Override
        public CharSequence getPageTitle(int position) {
            return MyPageTitle.get(position);
        }

        @Override
        public Fragment getItem(int i) {
            return MyFragment.get(i);
        }

        @Override
        public int getCount() {
            return 2;
        }
    }


    public void setUpViewPage(ViewPager viewPage) {
        ViewPageAdapter viewPageAdapter = new ViewPageAdapter(getSupportFragmentManager());
        viewPageAdapter.AddFragmentPage(new NurseFragment(), "NURSE");
        viewPageAdapter.AddFragmentPage(new PatientFragment(), "PATIENT");
        viewPage.setAdapter(viewPageAdapter);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        IntentResult result = IntentIntegrator.parseActivityResult(requestCode, resultCode, data);
        if (result != null) {
            if (result.getContents() == null) {
                Toast.makeText(this, "Result Not Found", Toast.LENGTH_LONG).show();
            } else {
                //todo: attendance send
            }
        } else {
            super.onActivityResult(requestCode, resultCode, data);
        }
    }

}
