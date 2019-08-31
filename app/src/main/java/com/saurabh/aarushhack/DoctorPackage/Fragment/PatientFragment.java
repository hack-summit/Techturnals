package com.saurabh.aarushhack.DoctorPackage.Activity.Fragment;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.ListView;

import androidx.fragment.app.Fragment;

import com.bumptech.glide.Glide;
import com.saurabh.aarushhack.R;


public class PatientFragment extends Fragment {

    View mainView;
    ListView listView;
    ImageView profieImage;

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        mainView = inflater.inflate(R.layout.fragment_recovered, container, false);
        listView = mainView.findViewById(R.id.listPatient);
        listView.setAdapter(new patientAdapter());
        return mainView;
    }

    public class patientAdapter extends BaseAdapter {

        @Override
        public int getCount() {
            return 10;
        }

        @Override
        public Object getItem(int i) {
            return null;
        }

        @Override
        public long getItemId(int i) {
            return 0;
        }

        @Override
        public View getView(int i, View view, ViewGroup viewGroup) {
            view = getLayoutInflater().inflate(R.layout.nurse_layout, null);
            profieImage = view.findViewById(R.id.profileImageMain);
            Glide.with(getActivity()).load("https://external-preview.redd.it/v-uKzKHVNLb-XsTt4umEJqYdq2Agaa6XDsV21V5XyN8.jpg?auto=webp&s=e02728abb9fc8d23affc911cf04381ac5ce50256").into(profieImage);
            view.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {

                }
            });
            return view;
        }
    }

}